#!/usr/bin/env python3
"""LEODAN local audio analyzer for WAV/MP3 files."""

from __future__ import annotations

import argparse
import datetime as dt
import math
from pathlib import Path

import librosa
import numpy as np
import soundfile as sf

try:
    import pyloudnorm as pyln
except Exception:  # optional dependency runtime fallback
    pyln = None


DEFAULT_REPORTS_DIR = Path("audio-tool/reports")


BANDS = [
    ("Sub", 20, 60),
    ("Bajo", 60, 250),
    ("Low mids", 250, 500),
    ("Mids", 500, 2000),
    ("Presencia", 2000, 6000),
    ("Aire", 6000, 16000),
]


def dbfs_from_linear(value: float, floor: float = 1e-12) -> float:
    return 20.0 * math.log10(max(value, floor))


def analyze_track(path: Path) -> dict:
    signal, sr = librosa.load(path, sr=None, mono=True)
    duration = len(signal) / sr if sr else 0.0

    peak_linear = float(np.max(np.abs(signal))) if len(signal) else 0.0
    rms_linear = float(np.sqrt(np.mean(np.square(signal)))) if len(signal) else 0.0
    peak_dbfs = dbfs_from_linear(peak_linear)
    rms_dbfs = dbfs_from_linear(rms_linear)

    lufs_note = ""
    if pyln is not None:
        try:
            meter = pyln.Meter(sr)
            lufs = float(meter.integrated_loudness(signal.astype(np.float64)))
        except Exception:
            lufs = rms_dbfs - 3.0
            lufs_note = "(estimado aprox. por fallback; pyloudnorm falló)"
    else:
        lufs = rms_dbfs - 3.0
        lufs_note = "(estimado aprox.; pyloudnorm no disponible)"

    tempo, _ = librosa.beat.beat_track(y=signal, sr=sr)
    bpm = float(np.squeeze(tempo)) if np.size(tempo) else 0.0

    house_hint = "Sin ajuste sugerido"
    if bpm < 90:
        house_hint = f"Doble tiempo sugerido: {bpm * 2:.2f} BPM"
        house_bpm = bpm * 2
    elif bpm > 160:
        house_hint = f"Medio tiempo sugerido: {bpm / 2:.2f} BPM"
        house_bpm = bpm / 2
    else:
        house_bpm = bpm

    stft = np.abs(librosa.stft(signal, n_fft=4096, hop_length=1024))
    freqs = librosa.fft_frequencies(sr=sr, n_fft=4096)
    power = np.mean(np.square(stft), axis=1)

    band_energy = {}
    total_energy = float(np.sum(power)) if len(power) else 0.0
    for label, low, high in BANDS:
        idx = np.where((freqs >= low) & (freqs < high))[0]
        energy = float(np.sum(power[idx])) if len(idx) else 0.0
        pct = (energy / total_energy * 100.0) if total_energy > 0 else 0.0
        band_energy[label] = pct

    if peak_dbfs > -3:
        headroom = "> -3 dBFS = poco margen de premaster"
    elif -6 <= peak_dbfs <= -3:
        headroom = "entre -6 y -3 dBFS = sano para premaster"
    elif peak_dbfs < -10:
        headroom = "< -10 dBFS = bajo pero usable"
    else:
        headroom = "margen intermedio usable"

    rec_premaster = []
    if peak_dbfs > -3:
        rec_premaster.append("Bajá el nivel de salida o limitador para recuperar headroom.")
    else:
        rec_premaster.append("Headroom razonable para procesar premaster.")
    rec_premaster.append("Controlá subgrave (20-60 Hz) para evitar bombeo excesivo.")

    rec_streaming = [
        "Apuntá a ~-14 LUFS integrados para plataformas streaming (aprox.).",
        "Chequeá que el true peak se mantenga por debajo de -1 dBTP en el master final.",
    ]

    rec_club = [
        "Para club/DJ set, priorizá pegada de bajo/kick y consistencia en 60-250 Hz.",
        "Podés masterizar más fuerte que streaming, pero evitá distorsión en transientes.",
    ]

    return {
        "path": path,
        "duration": duration,
        "sr": sr,
        "peak_dbfs": peak_dbfs,
        "rms_dbfs": rms_dbfs,
        "lufs": lufs,
        "lufs_note": lufs_note,
        "bpm": bpm,
        "house_bpm": house_bpm,
        "house_hint": house_hint,
        "bands": band_energy,
        "headroom": headroom,
        "rec_premaster": rec_premaster,
        "rec_streaming": rec_streaming,
        "rec_club": rec_club,
    }


def format_report(main: dict, reference: dict | None = None) -> str:
    lines = []
    lines.append("=== LEODAN AUDIO ANALYZER REPORT ===")
    lines.append(f"Archivo: {main['path']}")
    lines.append(f"Duración: {main['duration']:.2f} s")
    lines.append(f"Sample rate: {main['sr']} Hz")
    lines.append(f"Pico máximo: {main['peak_dbfs']:.2f} dBFS")
    lines.append(f"RMS: {main['rms_dbfs']:.2f} dBFS")
    lines.append(f"LUFS integrado: {main['lufs']:.2f} {main['lufs_note']}")
    lines.append(f"BPM estimado: {main['bpm']:.2f}")
    lines.append(f"BPM posible House/Tech House: {main['house_bpm']:.2f}")
    lines.append(f"Sugerencia BPM: {main['house_hint']}")
    lines.append("")
    lines.append("Distribución espectral (% energía aprox.):")
    for label, _, _ in BANDS:
        lines.append(f"- {label}: {main['bands'][label]:.2f}%")

    lines.append("")
    lines.append(f"Headroom: {main['headroom']}")

    lines.append("")
    lines.append("Recomendaciones - Premaster:")
    for r in main["rec_premaster"]:
        lines.append(f"- {r}")

    lines.append("")
    lines.append("Recomendaciones - Master streaming:")
    for r in main["rec_streaming"]:
        lines.append(f"- {r}")

    lines.append("")
    lines.append("Recomendaciones - Master club/DJ set:")
    for r in main["rec_club"]:
        lines.append(f"- {r}")

    if reference is not None:
        lines.append("")
        lines.append("Comparación con referencia:")
        lines.append(f"- Referencia: {reference['path']}")
        lines.append(f"- Delta pico (track - ref): {main['peak_dbfs'] - reference['peak_dbfs']:.2f} dB")
        lines.append(f"- Delta RMS (track - ref): {main['rms_dbfs'] - reference['rms_dbfs']:.2f} dB")
        lines.append(f"- Delta LUFS (track - ref): {main['lufs'] - reference['lufs']:.2f} LU")
        lines.append(f"- Delta BPM (track - ref): {main['bpm'] - reference['bpm']:.2f}")

    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analizador local de audio LEODAN")
    parser.add_argument("track", type=Path, help="Ruta al archivo principal WAV/MP3")
    parser.add_argument("--reference", type=Path, help="Ruta a archivo de referencia WAV/MP3")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_REPORTS_DIR,
        help="Directorio de salida para reportes TXT",
    )
    return parser.parse_args()


def validate_audio_file(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"No existe el archivo: {path}")
    if path.suffix.lower() not in {".wav", ".mp3"}:
        raise ValueError(f"Formato no soportado en {path}. Usá WAV o MP3.")
    sf.info(str(path))


def main() -> None:
    args = parse_args()
    validate_audio_file(args.track)
    if args.reference:
        validate_audio_file(args.reference)

    main_data = analyze_track(args.track)
    ref_data = analyze_track(args.reference) if args.reference else None

    report = format_report(main_data, ref_data)
    print(report, end="")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    out_name = f"reporte_{args.track.stem}_{timestamp}.txt"
    out_file = args.output_dir / out_name
    out_file.write_text(report, encoding="utf-8")
    print(f"Reporte guardado en: {out_file}")


if __name__ == "__main__":
    main()

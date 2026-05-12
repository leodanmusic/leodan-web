# LEODAN Audio Analyzer (local)

Herramienta local para analizar archivos WAV/MP3 orientada a flujos House/Tech House.

## 1) Instalación en Windows

1. Abrí PowerShell.
2. Parate en la raíz del repo (donde está este README).
3. Verificá Python 3.10+:
   ```powershell
   python --version
   ```

## 2) Crear entorno virtual

```powershell
python -m venv .venv-audio
.\.venv-audio\Scripts\Activate.ps1
```

## 3) Instalar dependencias

```powershell
pip install --upgrade pip
pip install -r requirements-audio-tool.txt
```

## 4) Uso base

```powershell
python tools/analyze_audio.py "audio-tool/tracks/mi_track.wav"
```

## 5) Uso con referencia

```powershell
python tools/analyze_audio.py "audio-tool/tracks/mi_track.wav" --reference "audio-tool/references/ref_track.wav"
```

## 6) Uso con output-dir

```powershell
python tools/analyze_audio.py "audio-tool/tracks/mi_track.wav" --output-dir "C:/Temp/reports"
```

## 7) Dónde poner tracks

Poné los temas a analizar en:

- `audio-tool/tracks/`

## 8) Dónde poner referencias

Poné temas de referencia (comerciales o masters previos) en:

- `audio-tool/references/`

## 9) Dónde se guardan reportes

Por defecto se guardan en:

- `audio-tool/reports/`

Nombre de salida:

- `reporte_<nombre_del_track>_<timestamp>.txt`

## 10) Ejemplo real House/Tech House

```powershell
python tools/analyze_audio.py "audio-tool/tracks/leodan_house_demo.mp3" --reference "audio-tool/references/house_ref.mp3"
```

El reporte muestra:

- Duración, sample rate, pico y RMS en dBFS.
- LUFS integrado (o estimación si falla `pyloudnorm`).
- BPM estimado + posible ajuste doble/medio tiempo.
- Distribución espectral por bandas (sub, bajo, mids, presencia, aire).
- Evaluación de headroom y recomendaciones para:
  - Premaster
  - Master streaming
  - Master club/DJ set

# LEODAN Codex Rules

Este documento establece las reglas operativas y de desarrollo para el proyecto web de LEODAN. Complementa a [AGENTS.md](file:///d:/LEODAN_WORKFLOW/03_Web/leodan-web-github/AGENTS.md) y [docs/brand.md](file:///d:/LEODAN_WORKFLOW/03_Web/leodan-web-github/docs/brand.md).

---

## 1. Entorno de Trabajo

*   **Repositorio Correcto:** Asegurar siempre que se está operando dentro del directorio de trabajo oficial:
    `D:\LEODAN_WORKFLOW\03_Web\leodan-web-github`
*   **Monitoreo Constante:** Es obligatorio ejecutar `git status` **antes y después** de cada cambio o conjunto de modificaciones para asegurar un árbol de trabajo limpio y prevenir commits erróneos.

---

## 2. Integridad del Código y Archivos

*   **Autorización de Archivos Core:** Queda estrictamente prohibido modificar los archivos base `index.html`, `links.html` y `style.css` sin autorización explícita de LEODAN.
*   **Políticas de Git (.gitignore):** No subir bajo ninguna circunstancia archivos de audio pesados (`*.wav`, `*.mp3`, `*.aiff`, `*.flac`) ni reportes/pistas generadas por herramientas locales (`audio-tool/reports/*`, `audio-tool/tracks/*`).
*   **Veracidad de Enlaces:** Queda terminantemente prohibido inventar enlaces (pre-saves, smart links, visualizers, etc.). Si un enlace no está explícitamente confirmado en `docs/brand.md` o por el artista, se debe usar un placeholder inactivo elegante (`aria-disabled="true"`).

---

## 3. Marca y Estética

*   **Fuente de la Verdad:** La guía oficial para identidad, voz, tono, paleta de colores y links oficiales es [docs/brand.md](file:///d:/LEODAN_WORKFLOW/03_Web/leodan-web-github/docs/brand.md).
*   **Estética Visual:** Todo desarrollo debe respetar la firma visual de LEODAN: oscura (`#040706`), verde elegante (`#72f8a4`), minimalista, espacial y con energía de club.
*   **Enfoque Mobile-First:** Priorizar siempre la experiencia móvil, ya que el principal canal de tráfico son las redes sociales (especialmente desde la biografía de Instagram: `https://leodan.net`).

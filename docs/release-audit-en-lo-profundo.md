# Informe de Auditoría y Plan de Lanzamiento: "En lo Profundo"

Este documento contiene el análisis estructural, técnico y de contenido para el próximo lanzamiento de **LEODAN**: **"En lo Profundo"**. Ha sido elaborado bajo el rol de *LEODAN Release Agent*, respetando estrictamente las reglas de marca, políticas del Codex y directrices estéticas definidas en el espacio de trabajo.

---

## 1. Estado General del Lanzamiento

El sistema de lanzamiento para **"En lo Profundo"** se encuentra actualmente en una **fase de pre-anuncio / preparación técnica**. 
La landing page ([en-lo-profundo.html](file:///d:/LEODAN_WORKFLOW/03_Web/leodan-web-github/en-lo-profundo.html)) cuenta con un esqueleto semántico excelente y una estética oscura y minimalista coherente, pero se mantiene en un estado pasivo. Prácticamente todas las acciones principales y secciones de contenido están basadas en placeholders inactivos (`aria-disabled="true"` y `"Link pendiente"`). 

El lanzamiento está listo a nivel conceptual y de diseño básico, pero requiere optimizaciones técnicas clave antes de recibir tráfico real desde las biografías de redes sociales (tráfico mobile-first).

---

## 2. Archivos Revisados

Para asegurar la máxima coherencia entre la marca, el código y la estrategia de marketing, se auditaron en profundidad los siguientes archivos del repositorio:

*   **Reglas de Trabajo y Operación:**
    *   [AGENTS.md](file:///d:/LEODAN_WORKFLOW/03_Web/leodan-web-github/AGENTS.md) — Reglas generales de marca, estética y frontend.
    *   [docs/codex-rules.md](file:///d:/LEODAN_WORKFLOW/03_Web/leodan-web-github/docs/codex-rules.md) — Reglas de entorno, integridad de código (restricción de archivos core y enlaces) y enfoque mobile-first.
*   **Identidad y Estrategia:**
    *   [docs/brand.md](file:///d:/LEODAN_WORKFLOW/03_Web/leodan-web-github/docs/brand.md) — La guía de estilo, paleta de colores oficial, links vigentes y pautas de redacción de LEODAN.
    *   [automations/release-checklist.md](file:///d:/LEODAN_WORKFLOW/03_Web/leodan-web-github/automations/release-checklist.md) — Lista de tareas operativas para cada fase del lanzamiento.
*   **Prompts de Generación de Contenido:**
    *   [prompts/spotify.md](file:///d:/LEODAN_WORKFLOW/03_Web/leodan-web-github/prompts/spotify.md) — Directrices de pitch, Canvas y copys.
    *   [prompts/instagram.md](file:///d:/LEODAN_WORKFLOW/03_Web/leodan-web-github/prompts/instagram.md) — Ideas de Reels, hooks y llamadas a la acción.
    *   [prompts/youtube.md](file:///d:/LEODAN_WORKFLOW/03_Web/leodan-web-github/prompts/youtube.md) — Conceptos audiovisuales y optimización de metadatos.
*   **Código Frontend y Landings:**
    *   [en-lo-profundo.html](file:///d:/LEODAN_WORKFLOW/03_Web/leodan-web-github/en-lo-profundo.html) — Estructura y estilos de la landing page del track.
    *   [index.html](file:///d:/LEODAN_WORKFLOW/03_Web/leodan-web-github/index.html) — Landing principal del artista (revisión de metatags y alineación).

---

## 3. Fortalezas Actuales

*   **Identidad Visual Impecable:** El archivo `en-lo-profundo.html` implementa a la perfección la paleta de colores oficial descrita en `brand.md` (negro profundo `#050806`, verde principal `#00ff88`, verde oscuro `#0b3d2e` y blanco frío `#e8f3ee`).
*   **Visual de Alta Estética CSS:** El elemento `.visual` genera una abstracción tridimensional muy atractiva (círculos en perspectiva, líneas de profundidad animadas y rejillas interactivas) sin necesidad de cargar imágenes pesadas, lo que garantiza una velocidad de carga móvil insuperable.
*   **Responsividad y Mobile-First:** El uso de `clamp()` para tipografía y la distribución de grid con media queries inteligentes (`min-width: 680px` y `min-width: 960px`) aseguran que la página se vea perfecta en cualquier pantalla táctil desde Instagram.
*   **Cumplimiento del Codex:** Todos los links inexistentes están marcados de forma segura con `aria-disabled="true"` e inactive states elegantes, evitando enlaces falsos o redirecciones rotas.
*   **Semántica y Accesibilidad:** Excelente uso de etiquetas HTML5 (`<header>`, `<main>`, `<section>`, `<article>`, `aria-labelledby`) para un SEO sólido y compatibilidad con lectores de pantalla.

---

## 4. Elementos Faltantes (Para que funcione como página de campaña)

1.  **Metadatos de Redes Sociales (SEO/Open Graph):**
    > [!WARNING]
    > `en-lo-profundo.html` carece de etiquetas Open Graph (`og:title`, `og:description`, `og:image`, `og:url`) y Twitter Cards. Si se comparte el enlace en WhatsApp, Instagram DMs o Twitter, se generará una vista previa vacía o genérica. Debe replicarse la estructura de metatags SEO de `index.html`.
2.  **Formulario de Captura de Emails:**
    Actualmente la página no cuenta con un sistema para captar correos electrónicos. Para un artista independiente, captar leads durante la fase de "Pre-save" es fundamental. Falta un bloque de suscripción elegante con el copy recomendado en `brand.md`.
3.  **Reproductor de Audio Teaser (Audio Preview):**
    Una página de lanzamiento es 10 veces más efectiva si el usuario puede escuchar un fragmento de 15-30 segundos de alta calidad directamente. Falta un reproductor de audio HTML5 minimalista o un widget integrado.
4.  **Lógica de Cambio de Fase (Pre-save vs. Lanzado):**
    No existe un mecanismo dinámico (JS o CSS) para alternar la landing entre la **Fase 1 (Pre-lanzamiento)** y la **Fase 2 (Ya disponible)**. Cuando el track se publique, habrá que reescribir manualmente varias secciones de código.
5.  **Artwork Oficial del Track:**
    Falta renderizar la imagen de la portada oficial (respetando la regla de mostrar *solo* el nombre del track "En lo Profundo") como un elemento visual central o de fondo sutil detrás de la animación CSS.

---

## 5. Textos y Copys Sugeridos para la Campaña

Para alimentar los canales principales de comunicación y las automatizaciones correspondientes, se han redactado los siguientes textos específicos y optimizados para LEODAN:

### A. Spotify (Pitch y Bio)
*   **Pitch para Editores (Spotify for Artists):**
    > *"LEODAN presenta 'En lo Profundo', una producción de House / Tech House que explora la tensión entre la introspección emocional y la intensidad de la pista. Con un groove constante, una línea de bajo hipnótica y atmósferas espaciales oscuras, este track marca una evolución sonora en mi catálogo independiente, orientada a clubs de sonido profundo y nocturno."* (380 caracteres - ideal para editores).
*   **Ideas de Canvas (Spotify loop):**
    *   *Concepto:* Un bucle vertical de 8 segundos que muestre una textura de rejilla en perspectiva verde neón moviéndose lentamente hacia un túnel oscuro, alineado con el pulso del drop del track.

### B. Instagram (Social Media)
*   **Versión Introspectiva/Oscura (Caption):**
    > *"Hay un punto en la noche donde la introspección se convierte en groove y la tensión empieza a moverse. 'En lo Profundo' es mi próximo track, creado desde ese territorio oscuro y elegante. Pre-save disponible en el link de la bio. https://leodan.net"*
*   **Versión Directa/Club (Caption):**
    > *"Diseñado para la pista, construido desde el groove y atmósferas espaciales. 'En lo Profundo' es mi nueva etapa sonora. Dale al pre-save en el link y aseguralo en tu biblioteca de Spotify. https://leodan.net"*
*   **Hook corto para Reels/Stories:**
    *   *"Menos ruido. Más intención. Entrá a lo profundo."*
    *   *"El pulso bajo la superficie."*

### C. YouTube (Metadatos y Descripciones)
*   **Título del Visualizer:** `LEODAN - En lo Profundo (Official Visualizer)`
*   **Descripción del Video:**
    > *"Escucha 'En lo Profundo', el nuevo single de LEODAN. House / Tech House con atmósfera oscura, elegante y espacial. 
    > 
    > 🟢 Escucha en Spotify: [LINK CONFIRMADO]
    > 🌐 Web Oficial: https://leodan.net
    > 📸 Instagram: @leodan_music
    > 
    > Producido de forma independiente en Uruguay. Todos los derechos reservados © 2026."*

### D. SoundCloud
*   **Título del Track:** `LEODAN - En lo Profundo (Original Mix)`
*   **Descripción:**
    > *"Conectando la profundidad emocional con la intensidad de la pista de club. 'En lo Profundo' continúa expandiendo mi universo sonoro mediante grooves marcados y atmósferas espaciales oscuras.
    > 
    > Escucha completa en Spotify y plataformas de streaming: [LINK CONFIRMADO]
    > Web Oficial: https://leodan.net"*

### E. Feature.fm / Smart Link
*   **Título:** `LEODAN - En lo Profundo`
*   **Subtexto en pre-lanzamiento:** `Pre-save el nuevo single de House / Tech House.`
*   **Subtexto en lanzamiento:** `Escuchar ahora en todas las plataformas.`

---

## 6. Assets Visuales Requeridos

Para completar la checklist de lanzamiento, se deben preparar los siguientes archivos con sus especificaciones técnicas:

| Asset | Formato / Dimensiones | Propósito | Estado / Detalle |
| :--- | :--- | :--- | :--- |
| **Portada Oficial** | PNG/JPG (3000 x 3000 px) | Distribución digital | Debe mostrar únicamente las palabras "En lo Profundo" (sin firma "LEODAN") |
| **Spotify Canvas** | MP4 (9:16 vertical, 8 seg, sin audio) | Loop visual en el reproductor | Estética verde y oscura de alto contraste |
| **Teaser Reel** | MP4 (9:16 vertical, 15-30 seg) | Promoción en Instagram y TikTok | Fragmento de audio del drop con tipografía animada |
| **Visualizer YouTube**| MP4 (16:9 horizontal, 1080p o 4K) | Video oficial en YouTube | Loop animado minimalista en base al concepto visual de la web |
| **Artwork de Prensa** | JPG (Landscape & Portrait, high res) | Dossier para sellos y prensa | Foto del artista con el tratamiento de color e iluminación espacial verde |

---

## 7. Automatizaciones Futuras Recomendadas

1.  **Captación de Leads (Email Service Integration):**
    Configurar un endpoint ligero y gratuito como **Formspree** o **Netlify Forms** conectado al formulario de la landing page para almacenar los correos captados en una base de datos segura de Mailchimp o Substack de manera automática.
2.  **Seguimiento y Retargeting (Píxeles de Conversión):**
    Insertar el píxel de Meta (Facebook Pixel) o Google Analytics en la cabecera de la landing page para medir cuántos usuarios de Instagram hacen clic en "Pre-save" y poder realizar anuncios de retargeting super segmentados.
3.  **Base de Datos en Notion para Gestión de Campañas:**
    Crear una base de datos centralizada en Notion conectada por Webhooks para automatizar el seguimiento de las fases del lanzamiento (Checklist de releases, links generados, estados de las redes y aprobaciones).

---

## 8. Secciones a Mejorar en el Futuro (en-lo-profundo.html)

*   **Fusión de la Animación CSS con el Video Background:** En lugar de una animación CSS abstracta rígida, integrar un fondo que intercale o cargue sutilmente fragmentos de video (o loops de Canvas) de fondo detrás de los textos.
*   **Implementación de Micro-Interacciones:** Agregar transiciones suaves en CSS (`transition: all 0.3s ease`) y efectos hover en los botones activos para elevar la sensación de "Premium" e interacción espacial de la página.
*   **Optimización del flujo de Pre-save directo:** En lugar de enviar al usuario a Feature.fm, integrar una API de pre-save directo dentro del propio sitio para que el usuario guarde el track sin salir de `leodan.net`.

---

## 9. Riesgos Identificados

*   **Riesgo de rebote por inactividad:** Compartir una página donde el 80% de los botones e items están "pendientes" puede frustrar al usuario. Se debe priorizar activar el formulario de emails para dar una acción con valor real inmediato.
*   **Falta de previsualización en redes (Riesgo SEO):** La carencia de Open Graph en `en-lo-profundo.html` restará profesionalismo al momento de compartir el enlace directamente.
*   **Incumplimiento de políticas de audio pesado:** Asegurar que los teasers o pre-escuchas que se integren en la web estén optimizados en peso (MP3 a 128kbps o 192kbps) y cargados desde un CDN, nunca subidos directamente al repositorio Git en formato WAV para cumplir con el Codex.

---

## 10. Próximos Pasos (Ordenados por Prioridad)

1.  **[Técnico - Alta Prioridad]** Agregar las etiquetas Meta SEO/Open Graph y estructuración semántica de compartición social a `en-lo-profundo.html`, usando como base los encabezados técnicos de `index.html`.
2.  **[Técnico - Alta Prioridad]** Diseñar e implementar el componente del formulario de captura de emails (Newsletter Box) en la zona inferior de la sección hero de la landing page, permitiendo que los usuarios se registren antes del lanzamiento oficial.
3.  **[Contenido - Media Prioridad]** Redactar y guardar en una carpeta local de la campaña los archivos finales de texto y copys correspondientes para cada red social (Spotify, Instagram, YouTube) basados en las plantillas generadas en esta auditoría.
4.  **[Diseño - Media Prioridad]** Desarrollar la interacción JS/CSS para cambiar la página de fase automáticamente en cuanto los links reales estén listos (alternando botones de "Pre-save" a "Streaming links").

---

## 11. Qué NO Tocar Todavía

> [!IMPORTANT]
> *   **No modificar los archivos Core:** `index.html`, `links.html`, `labels.html` y `style.css` deben mantenerse intactos y sin cambios de código hasta contar con la autorización correspondiente o pasar a la fase de integración de links oficiales.
> *   **No inventar ni mockear enlaces:** Los campos de links de Spotify, SoundCloud, etc., en `en-lo-profundo.html` deben seguir usando placeholders hasta que se obtengan los enlaces oficiales del distribuidor.
> *   **No subir archivos de audio pesados al Git:** Si se genera un audio teaser para la web, se debe colocar temporalmente en carpetas externas o gestionar adecuadamente a través de `.gitignore` según el Codex.

---

## Conclusión: ¿Está listo para pasar a Fase de Contenido?

**Sí**, el proyecto está listo conceptualmente y su estructura frontend base es excelente. Sin embargo, **desde la perspectiva de ingeniería y marketing, no se debe iniciar la fase de difusión masiva (Fase de Contenido) hasta que se completen los primeros dos pasos técnicos de la lista de prioridades** (Metatags de Open Graph y el bloque de captura de emails). 

Una vez resueltos estos dos aspectos, la landing page se convertirá en una máquina de conversión altamente profesional, lista para captar la atención del público internacional de LEODAN.

# Notion Setup Step 1: Content Calendar — En lo Profundo

## Objetivo

Crear manualmente en Notion la primera base de datos operativa del sistema de automatizacion de LEODAN:

**Content Calendar — En lo Profundo**

Esta base sirve para organizar contenidos de Instagram, TikTok, YouTube Shorts, Comunidad de YouTube y futuros posts de campana. El foco es ordenar ideas, assets, captions, fechas, links publicados y metricas sin activar todavia webhooks reales ni automatizaciones externas.

## Antes de empezar

- No pegar tokens, API keys ni credenciales en Notion.
- No crear webhooks reales desde este paso.
- No inventar links de Feature.fm, pre-save o landing si no estan confirmados.
- Usar placeholders cuando un link o asset aun no exista.
- Mantener el tono de campana de "En lo Profundo": oscuro, emocional, directo y energetico.

## Paso a paso en Notion

1. Abrir Notion y crear una nueva pagina.
2. Nombrar la pagina: `Content Calendar — En lo Profundo`.
3. Dentro de la pagina, elegir `Table - Full page` o `Table - Inline`.
4. Usar el mismo nombre para la base de datos: `Content Calendar — En lo Profundo`.
5. Crear las columnas indicadas en la seccion siguiente.
6. Configurar las opciones de select exactamente como se recomiendan.
7. Cargar las 10 filas iniciales de ejemplo.
8. Revisar cada pieza antes de programar o publicar.

## Columnas necesarias

| Columna | Tipo recomendado | Uso |
| --- | --- | --- |
| Titulo | Title | Nombre claro de la pieza de contenido. |
| Plataforma | Select | Canal donde se publicara. |
| Tipo de contenido | Select | Formato principal de la pieza. |
| Estado | Select | Etapa operativa del contenido. |
| Fecha de publicacion | Date | Fecha prevista o real de publicacion. |
| Link publicado | URL / Text | Link final cuando exista; placeholder si esta pendiente. |
| Track | Select / Text | Track asociado. |
| Campana | Select / Text | Campana de lanzamiento o promocion. |
| Objetivo | Select | Resultado buscado por la pieza. |
| Caption | Text | Copy final o borrador breve. |
| Asset necesario | Text | Video, portada, audio, visualizer o recurso pendiente. |
| Metrica principal | Select / Text | Indicador principal a revisar. |
| Notas | Text | Contexto, pendientes o aprendizaje. |

## Opciones recomendadas para selects

## Plataforma

- Instagram
- TikTok
- YouTube Shorts
- YouTube Comunidad
- SoundCloud
- Spotify
- Web

## Tipo de contenido

- Reel
- Short
- TikTok
- Story
- Comunidad
- Post
- Carrusel
- Visualizer
- Email
- Landing Update

## Estado

- Idea
- En produccion
- Programado
- Publicado
- Revisar metricas
- Reutilizar

## Objetivo

- Awareness
- Interaccion
- Pre-save
- Trafico a landing
- Comunidad
- Demo/Sellos

## Valores base de campana

- Track: `En lo Profundo`
- Campana: `en_lo_profundo_campaign`
- Link principal pendiente: `{{FEATUREFM_OR_LANDING_LINK_PLACEHOLDER}}`
- Carpeta de assets pendiente: `{{GOOGLE_DRIVE_ASSET_FOLDER_PLACEHOLDER}}`

## 10 filas de ejemplo

| Titulo | Plataforma | Tipo de contenido | Estado | Fecha de publicacion | Link publicado | Track | Campana | Objetivo | Caption | Asset necesario | Metrica principal | Notas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Reel teaser | Instagram | Reel | Idea | Pendiente | `{{POST_LINK_PLACEHOLDER}}` | En lo Profundo | en_lo_profundo_campaign | Awareness | Primer pulso de una etapa mas profunda. | Clip vertical 9:16 con fragmento del drop o tension previa. | Reproducciones | Mantener visual oscuro, verde y minimalista. |
| Historia con encuesta | Instagram | Story | Idea | Pendiente | `{{STORY_LINK_PLACEHOLDER}}` | En lo Profundo | en_lo_profundo_campaign | Interaccion | Que parte conecta mas: tension, groove o atmosfera? | Story 9:16 con encuesta nativa de Instagram. | Respuestas | Usar lenguaje breve y directo. |
| YouTube Short teaser | YouTube Shorts | Short | Idea | Pendiente | `{{SHORT_LINK_PLACEHOLDER}}` | En lo Profundo | en_lo_profundo_campaign | Awareness | Una mirada corta al lado mas intenso de LEODAN. | Video vertical con visualizer o estudio. | Retencion | Adaptar caption para busqueda en YouTube. |
| TikTok teaser | TikTok | TikTok | Idea | Pendiente | `{{TIKTOK_LINK_PLACEHOLDER}}` | En lo Profundo | en_lo_profundo_campaign | Awareness | Oscuro, directo, en movimiento. | Clip vertical con audio del track. | Visualizaciones | Probar un hook visual rapido en los primeros segundos. |
| Comunidad YouTube | YouTube Comunidad | Comunidad | Idea | Pendiente | `{{COMMUNITY_POST_LINK_PLACEHOLDER}}` | En lo Profundo | en_lo_profundo_campaign | Comunidad | En lo Profundo abre una energia mas intensa dentro del proyecto. | Imagen fija o frame del visualizer. | Interacciones | Texto breve, sin tono promocional generico. |
| Reel adelanto mas largo | Instagram | Reel | Idea | Pendiente | `{{POST_LINK_PLACEHOLDER}}` | En lo Profundo | en_lo_profundo_campaign | Trafico a landing | Una pieza creada desde la tension entre introspeccion y club. | Clip 20-30s con seccion fuerte del track. | Clics al perfil | CTA hacia `https://leodan.net` si corresponde. |
| Post portada | Instagram | Post | Idea | Pendiente | `{{POST_LINK_PLACEHOLDER}}` | En lo Profundo | en_lo_profundo_campaign | Awareness | En lo Profundo. Proxima etapa. | Portada con solo el nombre del track. | Guardados | Respetar regla de portada: solo nombre del tema. |
| Story proceso | Instagram | Story | Idea | Pendiente | `{{STORY_LINK_PLACEHOLDER}}` | En lo Profundo | en_lo_profundo_campaign | Comunidad | El sonido tambien se construye en la sombra. | Clip de estudio, DAW o textura visual. | Respuestas | Mostrar proceso sin revelar material sensible. |
| Reel storytelling | Instagram | Reel | Idea | Pendiente | `{{POST_LINK_PLACEHOLDER}}` | En lo Profundo | en_lo_profundo_campaign | Comunidad | En lo Profundo nace de ese punto donde la energia baja, pero la tension crece. | Video vertical con texto sobre imagen o visualizer. | Comentarios | Reforzar narrativa emocional y profesional. |
| Preparacion Feature.fm | Web | Landing Update | Idea | Pendiente | `{{FEATUREFM_SMART_LINK_PLACEHOLDER}}` | En lo Profundo | en_lo_profundo_campaign | Pre-save | Preparar smart link o pre-save cuando este confirmado. | Link validado, copy corto y asset de campana. | Clics | No publicar hasta confirmar Feature.fm o link oficial. |

## Como se conectara despues con n8n

En una fase posterior, n8n podra leer o actualizar esta base de Notion para:

- Crear tareas de contenido cuando un release pase a estado `anunciado`.
- Registrar links publicados cuando una pieza salga en redes.
- Guardar metricas por plataforma.
- Cambiar estado de `Publicado` a `Revisar metricas` despues de un periodo definido.
- Duplicar ideas exitosas hacia estado `Reutilizar`.
- Conectar futuras capturas de Feature.fm o landing con la campana correspondiente.

La conexion futura deberia usar variables seguras y credenciales guardadas dentro de n8n, nunca dentro del repositorio.

## Que NO automatizar todavia

- Publicacion directa en Instagram, TikTok o YouTube.
- Envio automatico de emails sin consentimiento verificado.
- Creacion de webhooks reales.
- Escritura automatica de captions finales sin revision humana.
- Reemplazo automatico de links oficiales.
- Cambios en HTML, CSS o imagenes de la web.
- Mensajes a sellos o contactos profesionales sin aprobacion previa.

## Proximo paso recomendado

Crear manualmente la base `Content Calendar — En lo Profundo` en Notion con estas columnas y cargar las 10 filas iniciales. Despues, revisar que estados, objetivos y captions funcionen para la campana antes de disenar cualquier flujo real en n8n.

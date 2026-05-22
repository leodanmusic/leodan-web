# Notion Schema

## Proposito

Disenar bases de datos futuras para organizar lanzamientos, contenido, demos, contactos, metricas y objetivos de sellos dentro del ecosistema operativo de LEODAN.

## Releases

| Columna | Tipo sugerido | Uso |
| --- | --- | --- |
| Name | title | Nombre del lanzamiento. |
| Track | text/select | Track asociado. |
| Release Status | select | demo, pendiente, anunciado, publicado, post-release. |
| Release Date | date | Fecha de lanzamiento. |
| Campaign | relation/text | Campana principal. |
| Smart Link | url/text | Link confirmado o placeholder. |
| Spotify Link | url/text | Link oficial cuando exista. |
| Press Notes | text | Narrativa breve para prensa. |
| Assets Folder | url/text | Carpeta en Google Drive o placeholder. |
| Notes | text | Observaciones internas. |

## Content Calendar

| Columna | Tipo sugerido | Uso |
| --- | --- | --- |
| Name | title | Nombre de la pieza. |
| Channel | select | Instagram, YouTube, TikTok, SoundCloud, Email, Press Kit. |
| Format | select | Reel, Short, post, story, email, nota. |
| Track | relation/text | Track relacionado. |
| Campaign | relation/text | Campana asociada. |
| Status | select | idea, guion, asset pendiente, programado, publicado, medido. |
| Publish Date | date | Fecha de publicacion. |
| CTA | text | Llamado a la accion. |
| Link Used | url/text | Link confirmado o placeholder. |
| Performance Notes | text | Lectura posterior de resultados. |

## Demo Submissions

| Columna | Tipo sugerido | Uso |
| --- | --- | --- |
| Name | title | Sello + track o envio. |
| Label | relation/text | Sello objetivo. |
| Contact | relation/text | Persona o email de contacto. |
| Track | text/select | Demo enviado. |
| Private Link | url/text | Link privado confirmado o placeholder. |
| Submission Date | date | Dia 0 del envio. |
| Follow-up Date | date | Dia 7 a 10 o dia 21. |
| Status | select | pendiente, enviado, follow-up 1, respondio, interesado, no interesado, sin respuesta. |
| Response | text | Respuesta recibida. |
| Notes | text | Contexto de negociacion o criterio editorial. |

## Contacts

| Columna | Tipo sugerido | Uso |
| --- | --- | --- |
| Name | title | Nombre de contacto. |
| Email | email | Correo. |
| Role | select | fan, A&R, curator, press, collaborator, label. |
| Source | select/text | Origen de captacion. |
| Consent Status | select | pending, granted, revoked, not_applicable. |
| Last Action | text | Ultimo contacto o evento registrado. |
| Last Contact Date | date | Fecha del ultimo contacto. |
| Campaign | relation/text | Campana relacionada. |
| Notes | text | Contexto relevante. |

## Campaign Metrics

| Columna | Tipo sugerido | Uso |
| --- | --- | --- |
| Name | title | Campana + fecha o canal. |
| Campaign | text/relation | Nombre interno de campana. |
| Track | text/relation | Track asociado. |
| Channel | select | Instagram, Feature.fm, Spotify, YouTube, SoundCloud, Email, Web. |
| Metric Type | select | clics, saves, opens, replies, plays, follows, conversions. |
| Metric Value | number | Valor numerico. |
| Date | date | Fecha de medicion. |
| Source Link | url/text | Link o placeholder de fuente. |
| Notes | text | Lectura cualitativa. |

## Label Targets

| Columna | Tipo sugerido | Uso |
| --- | --- | --- |
| Name | title | Nombre del sello. |
| Genre Fit | select | House, Tech House, Deep, Minimal, otro. |
| Priority | select | alta, media, baja. |
| Contact | relation/text | Contacto principal. |
| Submission Policy | text | Reglas publicas de envio si existen. |
| Last Submission | date | Ultimo envio realizado. |
| Current Status | select | investigar, listo, enviado, follow-up, respondio, descartado. |
| Notes | text | Encaje artistico y observaciones. |

# Content Repurposing Flow

## Objetivo

Convertir cada lanzamiento de LEODAN en un sistema de contenido coherente, mobile-first y medible, sin diluir la identidad oscura, elegante y energetica del proyecto.

## Entrada principal

Un lanzamiento confirmado, por ejemplo:

- Track: `En lo Profundo`
- Campana: `{{CAMPAIGN_ID_PLACEHOLDER}}`
- Asset base: `{{GOOGLE_DRIVE_ASSET_FOLDER_PLACEHOLDER}}`
- Link principal: `{{CONFIRMED_LINK_OR_PLACEHOLDER}}`

## Salidas por canal

| Canal | Formato | Objetivo | Estado inicial |
| --- | --- | --- | --- |
| Instagram | Reel | Impacto visual rapido y trafico hacia web o smart link. | idea |
| YouTube | Short | Refuerzo audiovisual y descubrimiento. | idea |
| TikTok | Video corto | Alcance y prueba de narrativa vertical. | idea |
| Comunidad YouTube | Post | Contexto directo para audiencia audiovisual. | idea |
| SoundCloud | Post/descripion | Escucha rapida cuando el track este validado para ese canal. | pendiente |
| Email | Newsletter | Conexion directa con seguidores y novedades. | idea |
| Press Kit | Nota breve | Material profesional para prensa, curadores y sellos. | idea |

## Flujo futuro

```text
Release confirmado
   |
   v
n8n crea tareas de contenido
   |
   v
Notion: Content Calendar
   |
   v
Revision de copy y assets
   |
   v
Publicacion por canal
   |
   v
Metricas y aprendizaje
```

## Campos recomendados para cada pieza

- `content_title`
- `track`
- `campaign`
- `channel`
- `format`
- `hook`
- `caption`
- `cta`
- `asset_status`
- `publish_date`
- `link_used`
- `status`
- `performance_notes`

## Reglas editoriales

- Evitar frases genericas de DJ.
- Mantener textos breves, con intencion y energia.
- Priorizar lectura movil.
- Usar `https://leodan.net` como referencia principal para Instagram cuando corresponda.
- No enlazar tracks o plataformas sin confirmacion oficial.

## Automatizaciones futuras

- Crear tareas automaticamente en Notion al marcar un release como anunciado.
- Generar checklist por canal.
- Recordar fechas de publicacion.
- Registrar metricas por pieza.
- Crear un resumen posterior de rendimiento por campana.

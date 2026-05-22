# n8n Roadmap

## Objetivo

Construir una arquitectura progresiva para que LEODAN pueda conectar datos de audiencia, lanzamientos, demos, contenido y metricas sin depender de procesos manuales dispersos.

## Fase 1: Estructura y datos

- Definir el mapa de datos minimo para emails, campanas, tracks, demos y metricas.
- Normalizar nombres de campos para evitar duplicados entre herramientas.
- Separar datos publicos, privados y pendientes de validacion.
- Crear criterios de estado: nuevo, pendiente, enviado, respondio, convertido, archivado.

## Fase 2: Notion / Google Sheets

- Crear bases operativas para releases, calendario de contenido, contactos, demos y metricas.
- Usar Google Sheets como respaldo liviano cuando convenga exportar o analizar rapidamente.
- Definir responsables de actualizacion manual mientras no haya automatizaciones activas.
- Preparar campos compatibles con n8n.

## Fase 3: Feature.fm y smart links

- Conectar eventos de smart link o pre-save con un webhook futuro de n8n.
- Registrar origen, campana, track, plataforma elegida y fecha.
- Enviar datos a Notion o Sheets.
- Preparar follow-up por email cuando exista consentimiento valido.

## Fase 4: Demo submissions

- Estructurar un flujo para contactos de sellos y solicitudes de demo.
- Registrar label, contacto, track, link privado pendiente o validado, fecha de envio y estado.
- Automatizar recordatorios de follow-up segun la cadencia: dia 0, dia 7 a 10, dia 21.
- Mantener trazabilidad sin exponer links privados en lugares publicos.

## Fase 5: Contenido automatico

- Convertir cada lanzamiento en una lista de piezas por canal.
- Crear tareas para Instagram Reel, YouTube Short, TikTok, Comunidad YouTube, SoundCloud, email y press kit.
- Registrar estado editorial: idea, guion, asset pendiente, programado, publicado, medido.
- Preparar repurposing desde un mismo concepto narrativo.

## Fase 6: Reporting

- Consolidar metricas por campana, track y canal.
- Comparar clics, saves, emails captados, respuestas de sellos y publicaciones realizadas.
- Generar reportes semanales o por lanzamiento.
- Detectar que canales empujan mejor la expansion internacional de LEODAN.

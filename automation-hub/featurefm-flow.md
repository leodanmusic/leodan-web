# Feature.fm Flow

## Objetivo

Definir un flujo futuro para conectar smart links o pre-saves de Feature.fm con n8n, Notion o Google Sheets, email follow-up y reporting de campana.

## Flujo previsto

```text
Feature.fm smart link / pre-save
        |
        v
n8n webhook futuro: {{N8N_FEATUREFM_WEBHOOK_PLACEHOLDER}}
        |
        v
Normalizacion de datos
        |
        v
Notion o Google Sheets
        |
        v
Email follow-up
        |
        v
Reporte de campana
```

## Eventos posibles

- Clic en smart link.
- Pre-save iniciado.
- Pre-save completado.
- Plataforma elegida: Spotify, Apple Music, YouTube, SoundCloud u otra.
- Email captado con consentimiento.
- Conversion desde una campana especifica.

## Campos minimos

- `event_type`
- `campaign_id`
- `track`
- `email`
- `platform_selected`
- `source`
- `timestamp`
- `smart_link_placeholder`
- `consent_status`

## Acciones en n8n

1. Recibir evento desde Feature.fm mediante webhook futuro.
2. Validar que el payload tenga los campos minimos.
3. Normalizar nombres de campos segun `automation-hub/data-map.md`.
4. Guardar el evento en Notion o Google Sheets.
5. Si existe consentimiento, enviar o programar un email follow-up.
6. Sumar el evento al reporte de campana.

## Placeholders seguros

- `{{N8N_FEATUREFM_WEBHOOK_PLACEHOLDER}}`
- `{{FEATUREFM_SMART_LINK_PLACEHOLDER}}`
- `{{FEATUREFM_PRESAVE_LINK_PLACEHOLDER}}`
- `{{EMAIL_AUTOMATION_PROVIDER_PLACEHOLDER}}`

## Notas

El smart link real o pre-save real debe ser confirmado por LEODAN antes de publicarse. Hasta entonces, cualquier referencia debe quedar como placeholder pendiente.

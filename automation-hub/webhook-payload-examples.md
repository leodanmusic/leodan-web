# Webhook Payload Examples

## Proposito

Ejemplos ficticios y seguros para disenar futuros webhooks de n8n. No contienen secretos, tokens, credenciales ni URLs reales.

## Email capture

```json
{
  "event_type": "email_capture",
  "email": "listener@example.test",
  "nombre": "Alex Rivera",
  "plataforma_origen": "instagram_bio",
  "campana": "en_lo_profundo_presave_phase_01",
  "track": "En lo Profundo",
  "fecha": "2026-06-01T18:30:00Z",
  "accion": "email_capture",
  "link_usado": "https://leodan.net",
  "respuesta": "consent_granted",
  "estado": "nuevo",
  "notas": "Registro ficticio para documentacion."
}
```

## Pre-save

```json
{
  "event_type": "pre_save",
  "email": "fan.presave@example.test",
  "nombre": "Mika Torres",
  "plataforma_origen": "featurefm_placeholder",
  "campana": "en_lo_profundo_presave_phase_01",
  "track": "En lo Profundo",
  "fecha": "2026-06-02T21:05:00Z",
  "accion": "pre_save_completed",
  "platform_selected": "spotify",
  "link_usado": "{{FEATUREFM_PRESAVE_LINK_PLACEHOLDER}}",
  "respuesta": "completed",
  "estado": "convertido",
  "notas": "Payload ficticio. Smart link pendiente de confirmacion."
}
```

## Demo request

```json
{
  "event_type": "demo_request",
  "email": "ar.contact@example.test",
  "nombre": "Jordan Vale",
  "label_name": "Example Label",
  "plataforma_origen": "labels_landing",
  "campana": "label_outreach_2026_q2",
  "track": "{{DEMO_TRACK_NAME_PLACEHOLDER}}",
  "fecha": "2026-06-03T14:20:00Z",
  "accion": "demo_request_received",
  "link_usado": "{{PRIVATE_DEMO_LINK_PLACEHOLDER}}",
  "respuesta": "pending_review",
  "estado": "pendiente_revision",
  "notas": "Ejemplo ficticio para flujo de sellos."
}
```

## Content published

```json
{
  "event_type": "content_published",
  "content_title": "En lo Profundo - teaser 01",
  "email": null,
  "nombre": null,
  "plataforma_origen": "instagram",
  "campana": "en_lo_profundo_release_phase",
  "track": "En lo Profundo",
  "fecha": "2026-06-04T19:00:00Z",
  "accion": "reel_published",
  "format": "instagram_reel",
  "link_usado": "{{PUBLIC_POST_LINK_PLACEHOLDER}}",
  "respuesta": "published",
  "estado": "publicado",
  "notas": "Post ficticio para registrar contenido publicado."
}
```

## Campaign metric

```json
{
  "event_type": "campaign_metric",
  "metric_id": "metric_example_001",
  "plataforma_origen": "featurefm_placeholder",
  "campana": "en_lo_profundo_presave_phase_01",
  "track": "En lo Profundo",
  "fecha": "2026-06-05T23:59:00Z",
  "accion": "daily_metric_snapshot",
  "metric_type": "smart_link_clicks",
  "metric_value": 128,
  "link_usado": "{{FEATUREFM_SMART_LINK_PLACEHOLDER}}",
  "respuesta": "snapshot_recorded",
  "estado": "medido",
  "notas": "Valor ficticio para ejemplo de reporte."
}
```

## Reglas para futuros payloads reales

- Reemplazar placeholders solo cuando LEODAN confirme integraciones.
- No incluir tokens, API keys ni secretos en payloads visibles.
- Mantener datos personales reales fuera del repositorio.
- Validar consentimiento antes de disparar emails.

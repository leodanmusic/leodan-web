# Demo Submission Flow

## Objetivo

Definir un flujo futuro para ordenar envios a sellos desde una landing orientada a decision rapida, manteniendo una comunicacion breve, profesional y segura.

## Flujo previsto

```text
labels.html
   |
   v
Contacto o demo request
   |
   v
n8n webhook futuro: {{N8N_DEMO_REQUEST_WEBHOOK_PLACEHOLDER}}
   |
   v
Notion: Demo Submissions / Contacts / Label Targets
   |
   v
Seguimiento
   |
   v
Respuesta
   |
   v
Estado final
```

## Entrada desde landing

La landing para sellos debe priorizar:

- Bio corta.
- Track destacado.
- Link privado o publico validado.
- Press kit.
- Contacto.
- Storytelling breve.

## Datos a capturar

- `label_name`
- `contact_name`
- `contact_email`
- `track`
- `private_link_placeholder`
- `source_page`
- `submission_intent`
- `timestamp`
- `notes`

## Estados del proceso

- `pendiente_envio`
- `enviado`
- `follow_up_1`
- `respondio`
- `interesado`
- `no_interesado`
- `sin_respuesta`
- `archivado`

## Cadencia recomendada

- Dia 0: envio inicial breve con identidad, track y link privado confirmado.
- Dia 7 a 10: primer follow-up directo, sin presion.
- Dia 21: cierre suave si no hubo respuesta.

## Acciones futuras en n8n

1. Recibir solicitud desde la landing o formulario futuro.
2. Validar que no falten contacto, track y consentimiento cuando aplique.
3. Crear o actualizar contacto en Notion.
4. Crear registro en Demo Submissions.
5. Programar recordatorio de follow-up.
6. Actualizar estado cuando exista respuesta.

## Seguridad

No incluir links privados reales en ejemplos publicos. Usar `{{PRIVATE_DEMO_LINK_PLACEHOLDER}}` hasta que LEODAN confirme el enlace.

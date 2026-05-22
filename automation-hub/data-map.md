# Data Map

## Proposito

Este documento define los datos clave que deberian viajar entre la web, Feature.fm, n8n, Notion, Google Sheets, email y reportes futuros.

## Campos principales

| Campo | Tipo sugerido | Descripcion | Ejemplo ficticio |
| --- | --- | --- | --- |
| email | email | Correo captado con consentimiento valido. | `listener@example.test` |
| nombre | texto | Nombre de la persona, sello o contacto. | `Alex Rivera` |
| plataforma_origen | texto | Canal desde donde llego la accion. | `instagram_bio` |
| campana | texto | Nombre interno de campana. | `en_lo_profundo_presave_phase_01` |
| track | texto | Track asociado a la accion. | `En lo Profundo` |
| fecha | fecha/hora | Momento de registro en formato ISO 8601. | `2026-06-01T18:30:00Z` |
| accion | texto | Evento realizado. | `email_capture` |
| link_usado | texto | Link publico, privado o placeholder usado. | `{{FEATUREFM_SMART_LINK_PLACEHOLDER}}` |
| respuesta | texto | Resultado, respuesta humana o estado de entrega. | `interesado_en_recibir_preview` |
| estado | select | Estado operativo del registro. | `nuevo` |
| notas | texto largo | Contexto adicional para seguimiento. | `Contacto entro desde una historia de Instagram.` |

## Estados recomendados

- `nuevo`
- `pendiente_revision`
- `enviado`
- `follow_up_1`
- `respondio`
- `interesado`
- `no_interesado`
- `convertido`
- `archivado`

## Reglas de seguridad

- No guardar tokens ni secretos dentro de payloads visibles en el repositorio.
- Usar placeholders para webhooks, smart links no confirmados y links privados pendientes.
- Los links oficiales confirmados deben validarse contra `docs/brand.md`.
- Los datos personales reales deben manejarse solo en herramientas autorizadas, no en ejemplos de documentacion.

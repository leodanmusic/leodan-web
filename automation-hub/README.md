# LEODAN Automation Hub

## Proposito

Automation Hub es el centro documental y tecnico para planificar futuras conexiones entre la web oficial de LEODAN, lanzamientos, Feature.fm, Notion, email, Google Drive y n8n.

Su objetivo es preparar una base clara para automatizar campanas, demos, captacion de emails y seguimiento de contenido sin modificar todavia la web publicada ni activar integraciones reales.

## Alcance

Este hub define:

- Datos clave que deberian viajar entre formularios, smart links, hojas de calculo y bases de datos.
- Flujos futuros para lanzamientos, demos, contenido y reporting.
- Estructuras recomendadas para Notion o Google Sheets.
- Ejemplos seguros de payloads JSON con datos ficticios.
- Reglas operativas para evitar credenciales, tokens o webhooks reales dentro del repositorio.

## Principios de trabajo

- No se documentan secretos ni credenciales.
- No se crean webhooks reales.
- No se inventan URLs finales de Feature.fm, n8n, Notion ni servicios externos.
- Los links oficiales siguen viviendo en `docs/brand.md`.
- Cualquier integracion futura debe respetar la identidad de LEODAN: oscura, elegante, directa, profesional y con vision internacional.

## Ecosistema previsto

```text
Web LEODAN / Feature.fm / Redes
        |
        v
   n8n webhook futuro
        |
        v
 Notion / Google Sheets / Drive
        |
        v
 Email follow-up / Reporting / Contenido
```

## Estado actual

Este directorio es una primera base de planificacion. No ejecuta automatizaciones por si mismo y no modifica la experiencia publica de la web.

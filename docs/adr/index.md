# Registro de decisiones (ADR)

Un ADR registra una decisión de arquitectura: el problema que la motivó, las opciones que se evaluaron, la opción elegida y sus consecuencias. Cada ADR es un archivo Markdown numerado en `docs/adr/`. Una decisión aceptada no se edita: si cambia, se escribe un ADR nuevo que la reemplaza y la anterior pasa a estado *reemplazada*.

| ID | Decisión | Estado | Fecha |
|---|---|---|---|
| [ADR-0000](0000-registrar-decisiones-con-madr.md) | Registrar las decisiones de arquitectura con MADR | Aceptada | 2026-11-01 |
| [ADR-0001](0001-api-de-consulta-entre-web-y-posventa.md) | Ubicar una API de Consulta entre la aplicación web y el Sistema de Posventa | Aceptada | 2026-11-01 |
| [ADR-0002](0002-autenticacion-con-proveedor-de-identidad.md) | Autenticar con un proveedor de identidad y crear el usuario en el primer ingreso | Aceptada | 2026-11-01 |
| [ADR-0003](0003-consulta-en-linea-sin-replica.md) | Consultar el Sistema de Posventa en línea, sin réplica de datos | Aceptada | 2026-11-01 |
| [ADR-0004](0004-documentacion-como-codigo.md) | Documentar la arquitectura como código con MkDocs y GitHub Pages | Aceptada | 2026-11-01 |

Para proponer una decisión nueva, copia la [plantilla](plantilla.md), asígnale el siguiente número y agrégala a esta tabla. El flujo de publicación valida que el ADR tenga los campos obligatorios.

---
status: aceptada
date: 2026-11-01
decision-makers: Cristian A. Acosta A.
---

# ADR-0003: Consultar el Sistema de Posventa en línea, sin réplica de datos

**Estado:** Aceptada · **Fecha:** 2026-11-01

## Contexto y planteamiento del problema

El portal muestra el estado de solicitudes que los colaboradores actualizan en el Sistema de Posventa. Hay que decidir si el portal lee esos datos en cada petición o guarda una copia propia.

## Factores de decisión

- RF-03: el estado mostrado coincide con el registrado en el momento de la consulta.
- RNF-02: el listado y el detalle cargan en 3 segundos o menos sin degradar el Sistema de Posventa.
- Evitar un segundo almacén de datos personales.

## Opciones consideradas

1. Consultar en línea en cada petición.
2. Replicar las solicitudes en una base de datos del portal con sincronización periódica.
3. Conectarse directamente a la base de datos del Sistema de Posventa.

## Resultado de la decisión

Opción elegida: "Consultar en línea en cada petición", porque muestra el estado vigente y el volumen esperado es bajo: un propietario consulta pocas solicitudes y de forma esporádica.

### Consecuencias

- Positiva: una sola fuente de verdad. No hay proceso de sincronización ni datos desactualizados.
- Positiva: los datos personales quedan en un solo lugar.
- Negativa: si el Sistema de Posventa no responde, el portal tampoco.
- Negativa: si el volumen crece, la API de Consulta es el punto donde agregar una caché. Ese cambio requeriría un ADR nuevo.

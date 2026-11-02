---
status: aceptada
date: 2026-11-01
decision-makers: Cristian A. Acosta A.
---

# ADR-0000: Registrar las decisiones de arquitectura con MADR

**Estado:** Aceptada · **Fecha:** 2026-11-01

## Contexto y planteamiento del problema

En la versión anterior del documento, las decisiones del portal estaban en una tabla dentro del HLD. Una tabla muestra la decisión final, pero pierde el contexto, las opciones descartadas y la fecha. Cuando una decisión cambió durante la revisión, la tabla se sobrescribió: la versión anterior quedó en el historial de la página, pero sin el motivo del cambio.

## Factores de decisión

- Conservar el porqué de cada decisión, no solo el resultado.
- Usar texto plano que se versione y se revise junto con el resto del repositorio.
- Seguir un formato conocido, con poco esfuerzo de escritura.

## Opciones consideradas

1. Tabla de decisiones dentro del HLD.
2. ADR con la plantilla de Michael Nygard (contexto, decisión, consecuencias).
3. ADR con MADR (Markdown Architectural Decision Records).

## Resultado de la decisión

Opción elegida: "ADR con MADR", porque agrega a la plantilla de Nygard las opciones consideradas y los factores de decisión, que son justo lo que se perdía en la tabla, y está pensada para Markdown dentro del repositorio.

### Consecuencias

- Positiva: cada decisión tiene su archivo, su historial en Git y su estado.
- Positiva: el HLD enlaza a los ADR en lugar de repetir la justificación.
- Negativa: escribir un ADR toma más tiempo que una fila de tabla.

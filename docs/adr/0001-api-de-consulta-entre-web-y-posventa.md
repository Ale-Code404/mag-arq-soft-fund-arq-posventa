---
status: aceptada
date: 2026-11-01
decision-makers: Cristian A. Acosta A.
---

# ADR-0001: Ubicar una API de Consulta entre la aplicación web y el Sistema de Posventa

**Estado:** Aceptada · **Fecha:** 2026-11-01

## Contexto y planteamiento del problema

La aplicación web necesita los datos de propietarios y solicitudes que guarda el Sistema de Posventa, un aplicativo interno que hoy solo usan los colaboradores. Hay que decidir por dónde llegan esos datos al navegador del propietario.

## Factores de decisión

- RNF-01: cada propietario ve solo sus solicitudes.
- El Sistema de Posventa es interno y no debe quedar expuesto a Internet.
- Un cambio en el Sistema de Posventa no debería obligar a cambiar el portal.

## Opciones consideradas

1. La aplicación web consulta directamente el Sistema de Posventa.
2. Una API lee la base de datos del Sistema de Posventa.
3. Una API de Consulta usa las consultas de solo lectura que expone el Sistema de Posventa.

## Resultado de la decisión

Opción elegida: "API de Consulta sobre las consultas de solo lectura", porque es la única que mantiene interno el Sistema de Posventa y aplica la regla de propiedad en el servidor.

### Consecuencias

- Positiva: la regla "cada propietario ve solo lo suyo" vive en el servidor. En el navegador podría alterarse.
- Positiva: la API traduce el modelo interno a un contrato propio. Un cambio en el Sistema de Posventa solo afecta a la API.
- Negativa: la constructora mantiene un servicio nuevo.
- Negativa: el Sistema de Posventa debe exponer dos consultas de solo lectura, si hoy no las tiene.

## Pros y contras de las opciones

| Opción | A favor | En contra |
|---|---|---|
| Web directo al Sistema de Posventa | No hay componente nuevo. | Expone el sistema interno y deja la regla de propiedad en el navegador. |
| API sobre la base de datos | No requiere cambios en el Sistema de Posventa. | Acopla el portal al esquema interno de la base de datos. |
| API sobre consultas de solo lectura | Sistema interno protegido, contrato estable. | Un servicio más y un cambio menor en el Sistema de Posventa. |

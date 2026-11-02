---
status: aceptada
date: 2026-11-01
decision-makers: Cristian A. Acosta A.
---

# ADR-0002: Autenticar con un proveedor de identidad y crear el usuario en el primer ingreso

**Estado:** Aceptada · **Fecha:** 2026-11-01

## Contexto y planteamiento del problema

El propietario debe probar quién es antes de ver sus solicitudes (RF-01). La constructora ya tiene su correo en el Sistema de Posventa, pero no tiene usuarios ni contraseñas para propietarios. Hay que decidir cómo se autentica y quién decide que la persona es propietaria.

## Factores de decisión

- El propietario consulta pocas veces: una contraseña se olvida.
- El correo registrado es el único dato confiable que ya existe.
- No crear un proceso de registro ni una sincronización nueva.
- No guardar credenciales en el portal.

## Opciones consideradas

1. Usuario y contraseña gestionados por el portal.
2. Número de documento y número de solicitud.
3. Proveedor de identidad con código al correo y usuarios registrados antes desde el Sistema de Posventa.
4. Proveedor de identidad con código al correo y usuario creado en el primer ingreso.
5. Código al correo construido en la API de Consulta, sin proveedor de identidad.

## Resultado de la decisión

Opción elegida: "Proveedor de identidad con usuario creado en el primer ingreso". El proveedor confirma que la persona controla el correo. La API de Consulta decide si es propietaria buscando ese correo en el Sistema de Posventa.

### Consecuencias

- Positiva: no hay contraseñas, formulario de registro ni sincronización de usuarios.
- Positiva: autenticación (quién eres) y autorización (qué te toca ver) quedan separadas.
- Negativa: una persona que no es propietaria puede validar su correo y quedar creada en el proveedor. No ve ningún dato: recibe el mensaje de orientación hacia servicio al cliente.
- Negativa: depende de que el correo del propietario esté actualizado en el Sistema de Posventa.

## Pros y contras de las opciones

| Opción | A favor | En contra |
|---|---|---|
| Usuario y contraseña | Modelo conocido. | Contraseñas olvidadas, credenciales guardadas en el portal. |
| Documento y número de solicitud | Sin registro. | Son datos que conocen terceros y no prueban identidad. |
| Usuarios registrados antes | Solo existen propietarios en el proveedor. | Sincronización entre sistemas y cambios de correo en dos lugares. |
| Usuario creado en el primer ingreso | Sin registro ni sincronización. | Cuentas de no propietarios en el proveedor, sin acceso a datos. |
| Código construido en la API | Un componente menos. | La constructora construye y mantiene la seguridad del inicio de sesión. |

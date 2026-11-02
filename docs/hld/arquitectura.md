# Arquitectura propuesta

La arquitectura se representa con dos diagramas. El diagrama de casos de uso muestra lo que el propietario hace en el portal. El diagrama de contenedores muestra las piezas de la solución y cómo se comunican. La fuente de ambos es `docs/diagramas/posventa.drawio`.

## Diagrama de casos de uso

![Figura 1. Diagrama de casos de uso](../diagramas/casos-uso.svg)

| Caso de uso | Actor principal | Requerimiento | Descripción |
|---|---|---|---|
| CU-01 Iniciar sesión | Propietario | RF-01, RNF-01 | El propietario ingresa su correo y recibe un código. El proveedor de identidad valida el código. La API de Consulta busca al propietario por ese correo en el Sistema de Posventa. |
| CU-02 Consultar mis solicitudes | Propietario | RF-02, RNF-01, RNF-02 | El propietario autenticado ve el listado de sus solicitudes. |
| CU-03 Ver detalle e historial | Propietario | RF-03, RNF-01, RNF-02 | Desde el listado, el propietario abre una solicitud y ve su estado actual y el historial de estados. Extiende CU-02. |

## Diagrama de contenedores

![Figura 2. Diagrama de contenedores](../diagramas/contenedores.svg)

El proveedor de identidad y el Sistema de Posventa se agrupan a la derecha porque la solución los usa sin construirlos.

## Componentes y responsabilidades

| Componente | Tipo | Responsabilidad | Tecnología general |
|---|---|---|---|
| Aplicación web | Contenedor nuevo | Presenta las pantallas de inicio de sesión, listado y detalle. No guarda datos de solicitudes. | Aplicación web servida por HTTPS. |
| API de Consulta | Contenedor nuevo | Verifica que el propietario inició sesión. Al abrir la sesión, busca al propietario en el Sistema de Posventa por su correo y guarda su identificador. Con ese identificador pide solo sus solicitudes y las entrega a la aplicación web en un formato propio. | Servicio REST sobre HTTPS. |
| Proveedor de identidad | Sistema externo | Envía el código de un solo uso al correo y confirma que la persona controla ese correo. Crea el usuario en su primer ingreso. No decide quién es propietario. | Servicio de identidad estándar. |
| Sistema de Posventa | Sistema existente | Conserva los propietarios, las solicitudes y sus estados. Expone dos consultas de solo lectura para la API de Consulta: buscar propietario por correo y consultar solicitudes por propietario. | Aplicativo interno actual. |

## Flujo principal de consulta

1. El propietario abre el portal e ingresa su correo.
2. La aplicación web redirige al proveedor de identidad, que envía un código al correo.
3. El propietario ingresa el código. El proveedor de identidad confirma su identidad, crea el usuario si es su primer ingreso y la aplicación web abre la sesión.
4. La aplicación web pide a la API de Consulta las solicitudes del propietario.
5. La API de Consulta verifica la sesión y busca al propietario por su correo en el Sistema de Posventa. Si no existe, responde con el mensaje de orientación hacia servicio al cliente y el flujo termina.
6. Si el propietario existe, la API de Consulta guarda su identificador en la sesión y pide al Sistema de Posventa sus solicitudes. Si no tiene ninguna, responde que no hay solicitudes registradas.
7. La aplicación web muestra el listado. Al seleccionar una solicitud, la API de Consulta pide el detalle y el historial con el mismo identificador del propietario.

## Trazabilidad con los requerimientos

| Requerimiento | Cómo lo cumple la arquitectura | Decisión relacionada |
|---|---|---|
| RF-01 | El proveedor de identidad confirma el correo y la API de Consulta busca al propietario en el Sistema de Posventa. | [ADR-0002](../adr/0002-autenticacion-con-proveedor-de-identidad.md) |
| RF-02, RF-03 | La API de Consulta lee del Sistema de Posventa en el momento de la petición. | [ADR-0001](../adr/0001-api-de-consulta-entre-web-y-posventa.md), [ADR-0003](../adr/0003-consulta-en-linea-sin-replica.md) |
| RNF-01 | El filtro por propietario se aplica en la API de Consulta y toda la comunicación usa HTTPS. | [ADR-0001](../adr/0001-api-de-consulta-entre-web-y-posventa.md) |
| RNF-02 | Cada consulta pide solo los registros de un propietario. | [ADR-0003](../adr/0003-consulta-en-linea-sin-replica.md) |

## Supuestos

- Cada propietario tiene un correo único registrado en el Sistema de Posventa. El colaborador lo registra y lo mantiene actualizado.
- El Sistema de Posventa expone, o puede exponer con un cambio menor, dos consultas de solo lectura: buscar un propietario por correo y consultar las solicitudes de un propietario con su historial de estados.
- La constructora tiene o contrata un proveedor de identidad que autentica con un código enviado al correo y crea el usuario en el primer ingreso.

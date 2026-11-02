# Requerimientos

## Funcionales

| ID | Requerimiento | Criterio de aceptación |
|---|---|---|
| RF-01 | El sistema debe autenticar al propietario mediante un código de un solo uso enviado al correo registrado en el Sistema de Posventa. | Un código vencido o incorrecto se rechaza. Un correo que no corresponde a un propietario no accede a ninguna solicitud y recibe el mensaje de orientación hacia servicio al cliente. |
| RF-02 | El sistema debe listar las solicitudes de posventa asociadas al propietario autenticado, con su número, inmueble, tipo y estado actual. | El listado muestra solo las solicitudes del propietario, ordenadas de la más reciente a la más antigua. Si el propietario no tiene solicitudes, el portal se lo informa. |
| RF-03 | El sistema debe mostrar el detalle de una solicitud seleccionada, con su estado actual y el historial de cambios de estado. | El estado mostrado coincide con el registrado en el Sistema de Posventa en el momento de la consulta. |

## No funcionales

| ID | Atributo de calidad | Requerimiento | Medida propuesta |
|---|---|---|---|
| RNF-01 | Seguridad (confidencialidad) | El propietario accede únicamente a sus propias solicitudes. Toda comunicación viaja cifrada. | Ningún propietario ve solicitudes de otro. Toda la comunicación usa HTTPS. |
| RNF-02 | Rendimiento | La consulta del listado y del detalle responde en un tiempo aceptable para el propietario sin degradar el Sistema de Posventa. | El listado y el detalle cargan en 3 segundos o menos. |

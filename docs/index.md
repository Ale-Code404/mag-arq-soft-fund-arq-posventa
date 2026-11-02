# Portal de Consulta de Posventa UAN

Documentación de arquitectura del portal donde el propietario de un inmueble entregado por la Constructora UAN consulta el estado de sus solicitudes de posventa. El sitio reúne la arquitectura de alto nivel (HLD) y el registro de decisiones de arquitectura (ADR).

| Campo | Valor |
|---|---|
| Materia | Fundamentos de Arquitectura de Software |
| Actividad | Módulo 4, Actividad 3 |
| Periodo | 2026-2 |
| Autor | Cristian A. Acosta A. |
| Caso | Constructora UAN, consulta de solicitudes de posventa |

## Contenido

| Sección | Qué contiene |
|---|---|
| [Arquitectura (HLD)](hld/index.md) | Necesidad, alcance, requerimientos, diagramas, componentes y conclusiones. |
| [Decisiones (ADR)](adr/index.md) | Cinco decisiones con su contexto, opciones consideradas y consecuencias. |
| [Cómo se construye](construccion.md) | Estructura del repositorio y automatización con GitHub Actions. |

## La solución en una frase

Una aplicación web y una API de Consulta permiten al propietario ver sus solicitudes con la información que ya existe en el Sistema de Posventa. Un proveedor de identidad confirma su correo con un código de un solo uso.

![Diagrama de contenedores](diagramas/contenedores.svg)

## Versiones

Cada versión publicada en [Releases](https://github.com/Ale-Code404/mag-arq-soft-fund-arq-posventa/releases) incluye el documento completo en PDF, generado de forma automática a partir de este sitio.

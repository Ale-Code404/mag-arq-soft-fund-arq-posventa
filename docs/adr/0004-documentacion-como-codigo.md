---
status: aceptada
date: 2026-11-01
decision-makers: Cristian A. Acosta A.
---

# ADR-0004: Documentar la arquitectura como código con MkDocs y GitHub Pages

**Estado:** Aceptada · **Fecha:** 2026-11-01

## Contexto y planteamiento del problema

La primera versión del HLD se publicó en Confluence. Funcionó para escribir y comentar, pero los diagramas quedaron como adjuntos fuera del historial, el Word de entrega se exportó a mano y los cambios de una decisión no quedaban ligados a su motivo. Hay que decidir dónde vive la documentación de arquitectura.

## Factores de decisión

- La documentación se versiona y se revisa igual que el código.
- Los diagramas tienen su fuente en el repositorio.
- Publicación y PDF de entrega sin pasos manuales.
- Herramienta abierta y usada por proyectos conocidos.

## Opciones consideradas

1. Confluence.
2. GitHub Pages con Jekyll, el generador por defecto.
3. GitHub Pages con MkDocs y el tema Material.
4. GitHub Pages con Docusaurus.

## Resultado de la decisión

Opción elegida: "GitHub Pages con MkDocs y el tema Material". La documentación es Markdown en `docs/`, la navegación se define en `mkdocs.yml` y GitHub Actions publica el sitio y genera el PDF.

### Consecuencias

- Positiva: cada cambio de la documentación es un commit revisable y cada versión entregada es un release.
- Positiva: los diagramas se exportan desde `posventa.drawio` en cada publicación, así que la imagen siempre corresponde a la fuente.
- Positiva: la compilación estricta falla si hay enlaces rotos y la validación de ADR falla si falta una sección obligatoria.
- Negativa: editar requiere Git y Markdown. Para personas sin ese hábito, Confluence es más directo.

## Más información

Proyectos que documentan con MkDocs: Backstage TechDocs (Spotify), Argo CD, FastAPI, Traefik y kOps (Kubernetes).

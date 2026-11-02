# Cómo se construye

Este sitio aplica documentación como código ([ADR-0004](adr/0004-documentacion-como-codigo.md)): el contenido es Markdown dentro del repositorio y GitHub Actions lo publica.

## Estructura del repositorio

```text
docs/
  index.md              Inicio
  hld/                  Arquitectura de alto nivel
  adr/                  Registro de decisiones (MADR)
  diagramas/
    posventa.drawio     Fuente de los diagramas (una página por figura)
mkdocs.yml              Configuración y navegación del sitio
scripts/
  validar_adr.py        Revisa campos y secciones obligatorias de cada ADR
  generar_pdf.py        Imprime el sitio en un PDF con Chromium
.github/
  actions/build-site/   Pasos comunes: diagramas, validación y compilación
  workflows/pages.yml   Publica el sitio en cada push a main
  workflows/release.yml Genera el PDF y crea el release con él
```

## Automatización

| Evento | Flujo | Pasos |
|---|---|---|
| Push a `main` | `pages.yml` | Exporta `posventa.drawio` a SVG, valida los ADR, compila con `mkdocs build --strict` y publica en GitHub Pages. |
| Etiqueta `v*` o release publicado | `release.yml` | Repite la compilación, imprime cada página en el orden del menú, une el resultado en un PDF con portada y crea el release con el PDF adjunto. |

La compilación estricta convierte en error cualquier enlace roto o imagen faltante. Si un ADR no tiene `status`, `date` o alguna sección obligatoria, la validación detiene la publicación.

## Trabajar en local

```bash
pip install -r requirements.txt
mkdocs serve
```

Los SVG de los diagramas los genera el flujo de publicación. Para verlos en local, exporta cada página de `posventa.drawio` desde draw.io como `casos-uso.svg` y `contenedores.svg` dentro de `docs/diagramas/`.

## Publicar una versión

1. Actualiza el contenido y haz push a `main`.
2. Crea y sube una etiqueta: `git tag v1.0.0 && git push origin v1.0.0`. También sirve crear el release desde GitHub.
3. El flujo crea el release y adjunta `HLD-ADR-Posventa-vX.Y.Z.pdf`.

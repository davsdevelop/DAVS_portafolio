# DAVS Portafolio

Portafolio personal desarrollado en **Python + Reflex**. Incluye páginas de presentación, experiencia, estudios, contacto y proyectos agrupados por tecnología.

## Requisitos

- Python **3.13**
- Node.js **24** (Reflex 0.11 requiere Node 22.22 o superior)
- Opcional: [uv](https://docs.astral.sh/uv/) para gestionar el entorno virtual

## Instalación y ejecución

```bash
# Crear entorno virtual
uv venv .venv --python 3.13

# Instalar dependencias
uv pip install --python .venv/bin/python -r requirements.txt

# Iniciar la aplicación
./run.sh
```

Abrir **http://localhost:3000**

`run.sh` usa npm como gestor del frontend (`REFLEX_USE_NPM=1`) para evitar fallos de Bun. También puedes ejecutar directamente:

```bash
source .venv/bin/activate
reflex run
```

## Estructura

```text
main/
  main.py              # Configuración de la app y rutas
  components/          # Navbar, footer, estilos y componentes
  pages/               # Páginas y subpáginas de proyectos
  information/         # Datos del portafolio en archivos JSON
assets/                # Imágenes, logos, videos y documentos
rxconfig.py            # Configuración de Reflex
requirements.txt       # Dependencias
reflex.lock/           # Lockfile del frontend
```

## Contenido

- Los textos, proyectos, estudios y experiencia se editan en `main/information/*.json`.
- Las imágenes y documentos se guardan en `assets/`.
- Los estilos reutilizables están en `main/components/style.py`.
- No editar `.web/`: es el frontend generado automáticamente por Reflex.

## Notas

- Al agregar imágenes, videos o PDFs nuevos, recuerda incluirlos en Git.
- Versión de Reflex fijada en `requirements.txt` (`reflex==0.11.0`).

## Licencia

Este proyecto es propietario y está protegido con **todos los derechos reservados**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

import reflex as rx
import json

from pathlib import Path
from ...components.paleta_colores import mi_paleta_colores
from ..style import (
    BODY, 
    COL_SPAN_1, 
    COL_SPAN_2, 
    GRID_3_COLS, 
    NAVBAR_LINK,
    BODY_HOME_PRESENTACION_BASE,
    BODY_HOME_PRESENTACION_FOTO_BASE,
    BODY_HOME_PRESENTACION_FOTO,
    BODY_HOME_PRESENTACION_TEXTO_SALUDO,
    BODY_HOME_PRESENTACION_TEXTO_MI_NOMBRE,
    BODY_HOME_PRESENTACION_TEXTO_BIOGRAFIA,
    BODY_HOME_PRESENTACION_TEXTO_CARGO,
    BODY_HOME_PROYECTOS_BASE,
    BODY_HOME_PROYECTOS_TITULO,
    BODY_HOME_PROYECTOS_SEPARATOR, 
    BODY_HOME_PROYECTOS_TECH_NAME_TEXT, 
    BODY_HOME_PROYECTOS_BASE_PROYECTOS,
    BODY_HOME_PROYECTOS_LOGO_IMG,
    BODY_HOME_PROYECTOS_BOTON_ANIMACION_BASE,
    )


RUTA_JSON = Path(__file__).resolve().parent.parent.parent / "information" / "informacion_personal.json"
with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
    INFORMACION_PERSONAL = json.load(archivo)


def proyecto_icon_with_separator(img_src: str, href: str, technology_name: str = "") -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("|", class_name=BODY_HOME_PROYECTOS_SEPARATOR),
            rx.box(
                rx.hstack(
                    rx.link(
                        rx.box(
                            rx.image(
                                src=img_src, 
                                class_name=BODY_HOME_PROYECTOS_LOGO_IMG,
                                alt=f"Logo {technology_name}"
                            ),
                            class_name=BODY_HOME_PROYECTOS_BOTON_ANIMACION_BASE,
                        ),
                        href=href, 
                        class_name=NAVBAR_LINK, 
                    ),
                    rx.text(
                        technology_name.upper(), 
                        class_name=BODY_HOME_PROYECTOS_TECH_NAME_TEXT
                    ),
                    align_items="center",
                ),
            ),
            spacing="0",
            align_items="center",
        ),
        class_name=BODY_HOME_PROYECTOS_BASE_PROYECTOS,
        position="relative",
    )


def body_home() -> rx.Component:
    return rx.box(
        # BODY 
        rx.box(
            # ************************************
            # CAJA IZQUIERDA (66% de la pantalla)
            # ************************************
            rx.box(
                # PRESENTACION
                rx.box(
                    rx.vstack(
                        # PRESENTACION - Fotografia - Saludo - Nombre
                        rx.box(
                            rx.hstack(
                                # PRESENTACION - Fotografia
                                rx.box(
                                    rx.image(src=INFORMACION_PERSONAL["personal"]["fotografia"], class_name=BODY_HOME_PRESENTACION_FOTO),
                                    class_name=BODY_HOME_PRESENTACION_FOTO_BASE
                                ),
                                # PRESENTACION - Saludo - Nombre
                                rx.box(
                                    rx.vstack(
                                        # PRESENTACION - Saludo
                                        rx.box(
                                            rx.text(INFORMACION_PERSONAL["personal"]["saludo"]),
                                            class_name=BODY_HOME_PRESENTACION_TEXTO_SALUDO
                                        ),
                                        # PRESENTACION - Nombre
                                        rx.box(
                                            rx.text(INFORMACION_PERSONAL["personal"]["nombre"]),
                                            class_name=BODY_HOME_PRESENTACION_TEXTO_MI_NOMBRE
                                        ),
                                        spacing="0",
                                    ),
                                ),
                                spacing="0",
                            ),
                        ),
                        # PRESENTACION - Biografia
                        rx.vstack(
                            # Cargo
                            rx.box(
                                rx.text(INFORMACION_PERSONAL["personal"]["cargo"]),
                                class_name=BODY_HOME_PRESENTACION_TEXTO_CARGO
                            ),
                            # Biografia
                            rx.text(INFORMACION_PERSONAL["personal"]["descripcion"]),
                            class_name=BODY_HOME_PRESENTACION_TEXTO_BIOGRAFIA
                        ),
                        spacing="0",
                    ),
                    class_name=BODY_HOME_PRESENTACION_BASE
                ),
                class_name=COL_SPAN_2, 
            ),

            # ************************************
            # CAJA DERECHA (33% de la pantalla)
            # ************************************
            rx.box(
                # PROYECTOS POR TECNOLOGÍA
                rx.box(
                    rx.vstack(
                        # PROYECTOS - TITULO (Mantenemos la estructura unificada que pediste)
                        rx.box(
                            rx.vstack(
                                rx.text("PROYECTOS POR TECNOLOGÍA"),
                                align_items="center", 
                                width="100%",
                                spacing="2",
                            ),
                            class_name=BODY_HOME_PROYECTOS_TITULO,
                        ),

                        # =========================================================================
                        # LLAMADAS AL COMPONENTE UNIFICADO 
                        # =========================================================================
                        
                        # 1. PYTHON
                        proyecto_icon_with_separator(
                            img_src="/logos/python_logo.png",
                            href="/proyectospython",
                            technology_name="Python"
                        ),

                        # 2. FASTAPI
                        proyecto_icon_with_separator(
                            img_src="/logos/fastapi_logo.png",
                            href="/proyectosfastapi",
                            technology_name="FastAPI"
                        ),

                        # 3. DJANGO
                        proyecto_icon_with_separator(
                            img_src="/logos/django_logo.png",
                            href="/proyectosdjango",
                            technology_name="Django"
                        ),

                        # 4. REFLEX
                        proyecto_icon_with_separator(
                            img_src="/logos/reflex_logo.png",
                            href="/proyectosreflex",
                            technology_name="Reflex"
                        ),

                        # 5. SQL
                        proyecto_icon_with_separator(
                            img_src="/logos/sql_logo.png",
                            href="/proyectossql",
                            technology_name="SQL"
                        ),
                        spacing="0",
                    ),
                    class_name=BODY_HOME_PROYECTOS_BASE,
                ),
                class_name=COL_SPAN_1, 
            ),
            class_name=GRID_3_COLS,
        ),
        class_name=BODY,
    )
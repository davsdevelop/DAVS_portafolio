import reflex as rx
import json
from pathlib import Path
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
    BODY_HOME_PRESENTACION_TEXTO_CARGO_DETALLE,
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

CARGO_COMPLETO = INFORMACION_PERSONAL["personal"]["cargo"]
CARGO_PRINCIPAL, _, CARGO_DETALLE = CARGO_COMPLETO.partition("(")
CARGO_PRINCIPAL = CARGO_PRINCIPAL.strip()
CARGO_DETALLE = f"({CARGO_DETALLE.strip()}" if CARGO_DETALLE else ""


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
        rx.box(
            # ************************************
            # CAJA IZQUIERDA (Presentación)
            # ************************************
            rx.box(
                rx.box(
                    rx.vstack(
                        # PRESENTACION - Fotografia - Saludo - Nombre
                        rx.box(
                            # Fotografia
                            rx.box(
                                rx.image(src=INFORMACION_PERSONAL["personal"]["fotografia"], class_name=BODY_HOME_PRESENTACION_FOTO),
                                class_name=BODY_HOME_PRESENTACION_FOTO_BASE
                            ),
                            # Saludo y Nombre
                            rx.box(
                                rx.vstack(
                                    rx.box(
                                        rx.text(INFORMACION_PERSONAL["personal"]["saludo"]),
                                        class_name=BODY_HOME_PRESENTACION_TEXTO_SALUDO
                                    ),
                                    rx.box(
                                        rx.text(INFORMACION_PERSONAL["personal"]["nombre"]),
                                        class_name=BODY_HOME_PRESENTACION_TEXTO_MI_NOMBRE
                                    ),
                                    spacing="0",
                                    align_items="center", 
                                ),
                                class_name="w-full md:w-auto flex flex-col items-center md:items-start"
                            ),
                            class_name="w-full flex flex-col md:flex-row items-center md:items-end justify-center md:justify-start",
                        ),
                        # PRESENTACION - Biografia
                        rx.vstack(
                            rx.box(
                                rx.vstack(
                                    rx.text(
                                        CARGO_PRINCIPAL.upper(),
                                        class_name=BODY_HOME_PRESENTACION_TEXTO_CARGO,
                                    ),
                                    rx.text(
                                        CARGO_DETALLE,
                                        class_name=BODY_HOME_PRESENTACION_TEXTO_CARGO_DETALLE,
                                    ),
                                    spacing="0",
                                    align_items="center",
                                    width="100%",
                                ),
                            ),
                            rx.text(INFORMACION_PERSONAL["personal"]["descripcion"]),
                            class_name=BODY_HOME_PRESENTACION_TEXTO_BIOGRAFIA
                        ),
                        spacing="0",
                        align_items="center", 
                    ),
                    class_name=BODY_HOME_PRESENTACION_BASE
                ),
                class_name=COL_SPAN_2, 
            ),

            # ************************************
            # CAJA DERECHA (Proyectos)
            # ************************************
            rx.box(
                rx.box(
                    rx.vstack(
                        # TÍTULO PRINCIPAL DE LA CAJA
                        rx.box(
                            rx.vstack(
                                rx.text("PROYECTOS POR TECNOLOGÍAS", text_align="center"),
                                align_items="center", 
                                justify_content="center",
                                width="100%",
                                spacing="2",
                            ),
                            class_name=BODY_HOME_PROYECTOS_TITULO,
                            width="100%", # Aseguramos que el contenedor del título ocupe todo el ancho
                        ),

                        # COLUMNAS HORIZONTALES
                        rx.hstack(
                            # --- COLUMNA 1: DATA SCIENCE & IA ---
                            rx.vstack(
                                rx.text("DATA SCIENCE & IA", font_weight="bold", margin_bottom="1em", white_space="nowrap"),
                                proyecto_icon_with_separator(img_src="/logos/python_logo.png", href="/proyectospython", technology_name="Python"),
                                proyecto_icon_with_separator(img_src="/logos/data.png", href="/proyectosdatayml", technology_name="Data y ML"),
                                proyecto_icon_with_separator(img_src="/logos/langchain_logo.png", href="/proyectoslangchainmcp", technology_name="LangChain/MCP"),
                                # proyecto_icon_with_separator(img_src="/logos/MCP_logo.png", href="/proyectosmcp", technology_name="MCP"),
                                proyecto_icon_with_separator(img_src="/logos/sql_logo.png", href="/proyectossql", technology_name="SQL"),
                                # proyecto_icon_with_separator(img_src="/logos/ML_logo.png", href="/proyectosML", technology_name="Machine Learning"),
                                spacing="0",
                                align_items="center", 
                            ),
                            
                            # --- COLUMNA 2: BACKEND E INTEGRACIÓN ---
                            rx.vstack(
                                rx.text("BACKEND E INTEGRACIÓN", font_weight="bold", margin_bottom="1em", white_space="nowrap"),
                                # proyecto_icon_with_separator(img_src="/logos/python_logo.png", href="/proyectospython", technology_name="Python"),
                                proyecto_icon_with_separator(img_src="/logos/fuse.png", href="/proyectosapachecamel", technology_name="APACHE CAMEL - FUSE"),
                                proyecto_icon_with_separator(img_src="/logos/fastapi_logo.png", href="/proyectosfastapi", technology_name="FastAPI"),
                                # proyecto_icon_with_separator(img_src="/logos/django_logo.png", href="/proyectosdjango", technology_name="Django"),
                                # proyecto_icon_with_separator(img_src="/logos/reflex_logo.png", href="/proyectosreflex", technology_name="Reflex"),
                                proyecto_icon_with_separator(img_src="/logos/nestjs_logo.png", href="/proyectosnestjs", technology_name="NestJS"),
                                # proyecto_icon_with_separator(img_src="/logos/react_logo.png", href="/proyectosreact", technology_name="React"),
                                spacing="0",
                                align_items="center", 
                            ),

                            gap="6rem", 
                            justify_content="center", 
                            width="100%",
                            align_items="start", 
                        ),
                        
                        spacing="0",
                        align_items="center", # ESTO CENTRA TODO EL CONJUNTO (TÍTULO Y COLUMNAS)
                        width="100%",
                    ),
                    
                    class_name=BODY_HOME_PROYECTOS_BASE,
                ),
                class_name=COL_SPAN_1, 
            ),
            class_name=GRID_3_COLS,
        ),
        class_name=f"{BODY} pt-10 md:pt-16 md:pr-16 lg:pr-24",
    )
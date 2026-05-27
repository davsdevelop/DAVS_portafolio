import reflex as rx
import json
from pathlib import Path

from ..style import (
    BODY, 
    PROYECTOS_HEADER_BASE, 
    PROYECTOS_HEADER_TITULO_PRINCIPAL,
    PROYECTOS_BODY_BASE, 
    PROYECTOS_CARD_BASE, 
    PROYECTOS_CARD_BASE_TITULO_CONTENEDOR,
    PROYECTOS_CARD_TITULO_TEXTO,
    PROYECTOS_CARD_TITULO_ICONOS,
    PROYECTOS_CARD_BASE_DESCRIPCION_CONTENEDOR,
    PROYECTOS_CARD_DESC_TEXTO,
    PROYECTOS_CARD_DESC_IMG_CAJA,
    PROYECTOS_CARD_DESC_IMG,
    PROYECTOS_CARD_ICONO_LINK,
)


RUTA_JSON = Path(__file__).resolve().parent.parent.parent / "information" / "informacion_proyectos.json"
with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
    INFORMACION_PROYECTOS = json.load(archivo)


def proyectos_reflex() -> rx.Component:
    return rx.box(
        rx.vstack(
            # 1. HEADER GENERAL DE LA PÁGINA
            rx.box(
                rx.heading("PROYECTOS REFLEX", class_name=PROYECTOS_HEADER_TITULO_PRINCIPAL), 
                class_name=PROYECTOS_HEADER_BASE,
            ),
            # 2. CONTENEDOR DE TARJETAS
            rx.box(
                # ==========================================
                # TARJETA PROYECTO 1
                # ==========================================
                rx.box(
                    # ---  HEADER DE LA TARJETA  ---
                    rx.box(
                        # Titulo Proyecto
                        rx.box(
                            rx.text(INFORMACION_PROYECTOS["proyecto_reflex_1"]["titulo"]),
                            class_name=PROYECTOS_CARD_TITULO_TEXTO,
                        ),
                        rx.box(
                             # Link a GitHub
                            rx.link(
                                rx.icon(tag="code", size=30),
                                href=INFORMACION_PROYECTOS["proyecto_reflex_1"]["link_repositorio"],
                                is_external=True,
                                class_name=PROYECTOS_CARD_ICONO_LINK,
                            ),
                            # Link a Web
                            rx.link(
                                rx.icon(tag="globe", size=30),
                                href=INFORMACION_PROYECTOS["proyecto_reflex_1"]["link_repositorio"],
                                is_external=True,
                                class_name=PROYECTOS_CARD_ICONO_LINK,
                            ),
                            class_name=PROYECTOS_CARD_TITULO_ICONOS,
                        ),
                        class_name=PROYECTOS_CARD_BASE_TITULO_CONTENEDOR,
                    ),
                    # --- CUERPO DE LA TARJETA  ---
                    rx.box(
                        # Descripcion Proyecto
                        rx.box(
                            rx.text(INFORMACION_PROYECTOS["proyecto_reflex_1"]["descripcion"], color="gray.300"),
                            class_name=PROYECTOS_CARD_DESC_TEXTO,
                        ),
                        rx.box(
                            # Imagen Proyecto
                            rx.image(
                                src=INFORMACION_PROYECTOS["proyecto_reflex_1"]["imagen"],
                                class_name=PROYECTOS_CARD_DESC_IMG,
                            ),
                            class_name=PROYECTOS_CARD_DESC_IMG_CAJA,
                        ),
                        class_name=PROYECTOS_CARD_BASE_DESCRIPCION_CONTENEDOR,
                    ),
                    class_name=PROYECTOS_CARD_BASE,
                ),

                # ==========================================
                # TARJETA PROYECTO 2
                # ==========================================
                rx.box(
                    # --- HEADER DE LA TARJETA  ---
                    rx.box(
                        # Título Proyecto
                        rx.box(
                            rx.text(INFORMACION_PROYECTOS["proyecto_reflex_2"]["titulo"]),
                            class_name=PROYECTOS_CARD_TITULO_TEXTO,
                        ),
                        rx.box(
                             # Link a GitHub
                            rx.link(
                                rx.icon(tag="code", size=30),
                                href=INFORMACION_PROYECTOS["proyecto_reflex_2"]["link_repositorio"],
                                is_external=True,
                                class_name=PROYECTOS_CARD_ICONO_LINK,
                            ),
                            # Link a Web
                            rx.link(
                                rx.icon(tag="globe", size=30),
                                href=INFORMACION_PROYECTOS["proyecto_reflex_2"]["link_repositorio"],
                                is_external=True,
                                class_name=PROYECTOS_CARD_ICONO_LINK,
                            ),
                            class_name=PROYECTOS_CARD_TITULO_ICONOS,
                        ),
                        class_name=PROYECTOS_CARD_BASE_TITULO_CONTENEDOR,
                    ),
                    # --- CUERPO DE LA TARJETA ---
                    rx.box(
                        # Descripcion Proyecto
                        rx.box(
                            rx.text(INFORMACION_PROYECTOS["proyecto_reflex_2"]["descripcion"], color="gray.300"),
                            class_name=PROYECTOS_CARD_DESC_TEXTO,
                        ),
                        rx.box(
                            # Imagen Proyecto
                            rx.image(
                                src=INFORMACION_PROYECTOS["proyecto_reflex_2"]["imagen"],
                                class_name=PROYECTOS_CARD_DESC_IMG,
                            ),
                            class_name=PROYECTOS_CARD_DESC_IMG_CAJA,
                        ),
                        class_name=PROYECTOS_CARD_BASE_DESCRIPCION_CONTENEDOR,
                    ),
                    class_name=PROYECTOS_CARD_BASE,
                ),
                    
                class_name=PROYECTOS_BODY_BASE,
            ),
            spacing="0",
            width="100%",
        ),
        class_name=BODY,
    )
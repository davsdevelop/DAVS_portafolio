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
    PROYECTOS_CARD_DESC_IMG_ZOOM,
    PROYECTOS_CARD_DESC_IMG_ZOOM_CERRAR,
)

RUTA_JSON = Path(__file__).resolve().parent.parent.parent / "information" / "informacion_proyectos.json"
with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
    INFORMACION_PROYECTOS = json.load(archivo)


def card_proyecto(datos: dict) -> rx.Component:
    tiene_app = bool(datos.get("link_app", ""))
    
    iconos_children = [
        rx.link(
            rx.icon(tag="code", size=30),
            href=datos["link_repositorio"],
            is_external=True,
            class_name=PROYECTOS_CARD_ICONO_LINK,
        ),
    ]
    if tiene_app:
        iconos_children.append(
            rx.link(
                rx.icon(tag="globe", size=30),
                href=datos["link_app"],
                is_external=True,
                class_name=PROYECTOS_CARD_ICONO_LINK,
            )
        )

    return rx.box(
        rx.vstack(
            rx.flex(
                rx.box(
                    rx.text(datos["titulo"]),
                    class_name=PROYECTOS_CARD_TITULO_TEXTO,
                ),
                rx.box(
                    *iconos_children,
                    class_name=PROYECTOS_CARD_TITULO_ICONOS,
                ),
                direction={"initial": "column", "md": "row"},
                class_name=PROYECTOS_CARD_BASE_TITULO_CONTENEDOR,
            ),
            rx.flex(
                rx.box(
                    rx.text(datos["descripcion"]),
                    class_name=PROYECTOS_CARD_DESC_TEXTO,
                ),
                
                # INICIO DEL CAMBIO: Contenedor de la Imagen con Zoom
                rx.box(
                    rx.dialog.root(
                        rx.dialog.trigger(
                            rx.image(
                                src=datos["imagen"], 
                                class_name=PROYECTOS_CARD_DESC_IMG
                            ),
                        ),
                        rx.dialog.content(
                            rx.vstack(
                                rx.image(
                                    src=datos["imagen"],
                                    class_name=PROYECTOS_CARD_DESC_IMG_ZOOM
                                ),
                                rx.dialog.close(
                                    rx.button(
                                        "Cerrar", 
                                        class_name=PROYECTOS_CARD_DESC_IMG_ZOOM_CERRAR
                                    )
                                ),
                                align_items="center",
                                spacing="0"
                            ),
                            background_color="#0E151F",
                            border="2px solid #00D1B3",
                            max_width="45vw",
                            width="45vw",
                            class_name="rounded-xl shadow-2xl p-4"
                        ),
                    ),
                    class_name=PROYECTOS_CARD_DESC_IMG_CAJA,
                ),
                # FIN DEL CAMBIO
                
                direction={"initial": "column", "md": "row"},
                class_name=PROYECTOS_CARD_BASE_DESCRIPCION_CONTENEDOR,
            ),
            spacing="0",
        ),
        class_name=PROYECTOS_CARD_BASE,
    )


def proyectos_sql() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.heading("PROYECTOS SQL", class_name=PROYECTOS_HEADER_TITULO_PRINCIPAL),
                class_name=PROYECTOS_HEADER_BASE,
            ),
            rx.box(
                card_proyecto(INFORMACION_PROYECTOS["proyecto_sql_1"]),
                card_proyecto(INFORMACION_PROYECTOS["proyecto_sql_2"]),
                class_name=PROYECTOS_BODY_BASE,
            ),
            spacing="0",
            width="100%",
        ),
        class_name=BODY,
    )
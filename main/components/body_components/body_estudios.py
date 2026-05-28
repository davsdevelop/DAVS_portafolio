import reflex as rx
import json
from pathlib import Path

from ..style import (
    BODY, 
    ESTUDIOS_HEADER_BASE, 
    ESTUDIOS_HEADER_TITULO_PRINCIPAL,
    ESTUDIOS_BODY_BASE, 
    ESTUDIOS_CARD_BASE, 
    ESTUDIOS_CARD_HEADER_GRUPO_BOX,
    ESTUDIOS_CARD_HEADER_GRUPO_TITULO,
    ESTUDIOS_CARD_HEADER_GRUPO_TITULO_TEXT,
    ESTUDIOS_CARD_ROW_FECHA_TEXT,
    ESTUDIOS_CARD_ROW_TITULO_INST_TEXT,
    ESTUDIOS_CARD_ROW_LINK_CERT_ICON,
)

# --- MOTOR DE LECTURA DE DATOS ---
RUTA_JSON = Path(__file__).resolve().parent.parent.parent / "information" / "informacion_estudios.json"
with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
    INFORMACION_ESTUDIOS = json.load(archivo)

def crear_fila_estudio(datos: dict) -> rx.Component:
    links = [v for k, v in datos.items() if "link_certificado" in k and v]
    return rx.flex(
        rx.box(
            rx.text(datos["fecha_inicio"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
            rx.text(datos["fecha_fin"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
            class_name="w-full md:w-[20%] p-2",
        ),
        rx.box(
            rx.text(datos["titulo"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
            rx.text(datos["institucion"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
            class_name="w-full md:w-[60%] p-2",
        ),
        rx.hstack(
            *[
                rx.link(
                    rx.icon("file-badge", size=24, class_name=ESTUDIOS_CARD_ROW_LINK_CERT_ICON),
                    href=link,
                    is_external=True
                ) for link in links
            ],
            class_name="w-full md:w-[20%] p-2 justify-center md:justify-end gap-2",
        ),
        direction={"initial": "column", "md": "row"},
        align="center",
        class_name="border-b border-gray-800 p-2",
    )

def body_estudios() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.heading("ESTUDIOS", class_name=ESTUDIOS_HEADER_TITULO_PRINCIPAL),
                class_name=ESTUDIOS_HEADER_BASE,
            ),
            
            # TARJETA 1
            rx.box(
                rx.box(
                    rx.text(INFORMACION_ESTUDIOS["grupo1"]["titulo"], class_name=ESTUDIOS_CARD_HEADER_GRUPO_TITULO_TEXT),
                    class_name=ESTUDIOS_CARD_HEADER_GRUPO_TITULO,
                ),
                crear_fila_estudio(INFORMACION_ESTUDIOS["estudio_1_1"]),
                crear_fila_estudio(INFORMACION_ESTUDIOS["estudio_1_2"]),
                crear_fila_estudio(INFORMACION_ESTUDIOS["estudio_1_3"]),
                class_name=ESTUDIOS_CARD_BASE,  # ← keyword al final
            ),

            # TARJETA 2
            rx.box(
                rx.box(
                    rx.text(INFORMACION_ESTUDIOS["grupo2"]["titulo"], class_name=ESTUDIOS_CARD_HEADER_GRUPO_TITULO_TEXT),
                    class_name=ESTUDIOS_CARD_HEADER_GRUPO_TITULO,
                ),
                crear_fila_estudio(INFORMACION_ESTUDIOS["estudio_2_1"]),
                crear_fila_estudio(INFORMACION_ESTUDIOS["estudio_2_2"]),
                crear_fila_estudio(INFORMACION_ESTUDIOS["estudio_2_3"]),
                crear_fila_estudio(INFORMACION_ESTUDIOS["estudio_2_4"]),
                crear_fila_estudio(INFORMACION_ESTUDIOS["estudio_2_5"]),
                crear_fila_estudio(INFORMACION_ESTUDIOS["estudio_2_6"]),
                class_name=ESTUDIOS_CARD_BASE,  # ← keyword al final
            ),
            spacing="0",
            width="100%",
            class_name=ESTUDIOS_BODY_BASE,      # ← keyword al final
        ),
        class_name=BODY,
    )
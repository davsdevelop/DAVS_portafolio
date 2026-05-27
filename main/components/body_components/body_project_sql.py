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


def proyectos_sql() -> rx.Component:
    return rx.box(
        rx.vstack(
            # 1. HEADER GENERAL DE LA PÁGINA
            rx.box(
                rx.heading("PROYECTOS SQL", class_name=PROYECTOS_HEADER_TITULO_PRINCIPAL), 
                class_name=PROYECTOS_HEADER_BASE,
            ),
            
            # 2. CONTENEDOR DE TARJETAS
            rx.box(

                # AQUI TARJETAS
                    
            class_name=PROYECTOS_BODY_BASE,
            ),
            spacing="0",
            width="100%",
        ),
        class_name=BODY,
    )
import reflex as rx
import json

from pathlib import Path
from ..style import (
    BODY, 
    ML_HEADER_TITULO_PRINCIPAL, 
    ML_BODY_BASE, 
    ML_BODY_FOTO, 
    ML_BODY_FOTO_BASE,
    ML_CARD_BASE, 
    ML_BOTON_ANIMACION_BASE, 
    ML_LOGO_IMG,             
    ML_TEXTO_LINK,
    ML_LOGO_ICON,
    ML_TEXTO_NORMAL
    )


RUTA_JSON = Path(__file__).resolve().parent.parent.parent / "information" / "informacion_personal.json"
with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
    INFORMACION_PERSONAL = json.load(archivo)



def fila_ml(elemento_grafico: rx.Component | None, texto: str, href: str | None = None) -> rx.Component:
    
    # Decidimos qué clase de texto usar: si hay href, usa el estilo con hover, si no, el normal
    clase_texto = ML_TEXTO_LINK if href else ML_TEXTO_NORMAL

    # Creamos el contenido interno
    contenido = rx.hstack(
        rx.box(
            elemento_grafico,
            class_name=ML_BOTON_ANIMACION_BASE,
            display="none" if elemento_grafico is None else "flex" 
        ),
        # Aplicamos la clase dinámica aquí
        rx.text(texto, class_name=clase_texto, text_align="center"),
        align_items="center",
        justify_content="center",
        spacing="6" if elemento_grafico else "0",
        width="100%"
    )

    # Si existe una URL, envolvemos el contenido en un link
    if href:
        return rx.link(
            contenido,
            href=href,
            is_external=True, 
            _hover={"text_decoration": "none"},
            width="100%" 
        )
    
    # Si no hay URL, devolvemos el contenido estático (sin hover ni manito)
    return contenido


def body_ml() -> rx.Component:
    return rx.box(
        rx.box(
            rx.heading("MACHINE LEARNING & REDES NEURONALES", class_name=ML_HEADER_TITULO_PRINCIPAL), 
            rx.box(
                rx.vstack(
                    # FOTOGRAFÍA
                    rx.box(
                        rx.image(src=INFORMACION_PERSONAL["blog"]["fotografia"], class_name=ML_BODY_FOTO),
                        class_name=ML_BODY_FOTO_BASE
                    ),
                    
                    # CONTENIDO DE TEXTO
                    rx.vstack(
                        # FILA TITULO 
                        fila_ml(
                            elemento_grafico=None, 
                            texto=INFORMACION_PERSONAL["blog"]["titulo"], 
                        ),
                        # FILA DESCRIPCION 
                        fila_ml(
                            elemento_grafico=None, 
                            texto=INFORMACION_PERSONAL["blog"]["descripcion"],
                        ),
                        rx.spacer(),
                        # FILA UBICACION / BLOG
                        fila_ml(
                            elemento_grafico=rx.icon(tag="link", size=28, class_name=ML_LOGO_ICON), 
                            texto="neuromblog.blogspot.com", 
                            href=INFORMACION_PERSONAL["blog"]["blog_link"],
                        ),
                        align_items="center", # <-- CAMBIADO A "center"
                        width="100%",         # <-- AÑADIDO para asegurar centrado
                        spacing="5",          # <-- Ajustado para mejor distribución
                    ),
                    align_items="center",
                    width="100%",
                ),
                class_name=ML_CARD_BASE,
            ),
            class_name=ML_BODY_BASE
        ),
        class_name=BODY,
    )
import reflex as rx
import json

from pathlib import Path
from ..style import (
    BODY, 
    CONTACTO_HEADER_TITULO_PRINCIPAL, 
    CONTACTO_BODY_BASE, 
    CONTACTO_BODY_FOTO, 
    CONTACTO_BODY_FOTO_BASE,
    CONTACTO_CARD_BASE, 
    CONTACTO_BOTON_ANIMACION_BASE, 
    CONTACTO_LOGO_IMG,             
    CONTACTO_TEXTO_LINK,
    CONTACTO_LOGO_ICON
    )


RUTA_JSON = Path(__file__).resolve().parent.parent.parent / "information" / "informacion_personal.json"
with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
    INFORMACION_PERSONAL = json.load(archivo)



def fila_contacto(elemento_grafico: rx.Component, texto: str, href: str | None = None) -> rx.Component:
    contenido = rx.hstack(
        rx.box(
            elemento_grafico,
            class_name=CONTACTO_BOTON_ANIMACION_BASE,
        ),
        rx.text(texto, class_name=CONTACTO_TEXTO_LINK),
        align_items="center",
        spacing="4", 
        max_width="100%",
    )
    if not href:
        return contenido
    es_archivo = href.startswith(("/documentos/", "/videos/", "/imagenes/"))
    return rx.link(
        contenido,
        href=href,
        is_external=href.startswith("http") or es_archivo,
        display="flex",
        justify_content="flex-start",
        _hover={"text_decoration": "none"} 
    )


def body_contacto() -> rx.Component:
    return rx.box(
        rx.box(
            rx.heading("CONTACTO", class_name=CONTACTO_HEADER_TITULO_PRINCIPAL), 
            rx.box(
                rx.vstack(
                    # FOTOGRAFÍA
                    rx.box(
                        rx.image(
                            src=INFORMACION_PERSONAL["personal"]["fotografia"],
                            alt=f"Fotografía de {INFORMACION_PERSONAL['personal']['nombre']}",
                            class_name=CONTACTO_BODY_FOTO,
                        ),
                        class_name=CONTACTO_BODY_FOTO_BASE
                    ),
                    rx.vstack(
                        # FILA EMAIL 
                        fila_contacto(
                            elemento_grafico=rx.icon(tag="mail", size=28, class_name=CONTACTO_LOGO_ICON), 
                            texto=INFORMACION_PERSONAL["personal"]["davs_email"], 
                            href=f"mailto:{INFORMACION_PERSONAL['personal']['davs_email']}",
                        ),
                        # FILA LINKEDIN 
                        fila_contacto(
                            elemento_grafico=rx.image(
                                src="/logos/linkedin_logo.png",
                                alt="Logo de LinkedIn",
                                color="#46AC9F",
                                class_name=CONTACTO_LOGO_IMG,
                            ), 
                            texto="linkedin/diegovidela-dev", 
                            href=INFORMACION_PERSONAL["personal"]["linkedin_link"]
                        ),
                        # FILA UBICACION 
                        fila_contacto(
                            elemento_grafico=rx.icon(tag="map-pin", size=28, class_name=CONTACTO_LOGO_ICON), 
                            texto=INFORMACION_PERSONAL["personal"]["davs_ubicacion"],
                        ),
                        # FILA CV 
                        fila_contacto(
                            elemento_grafico=rx.icon(tag="file-text", size=28, class_name=CONTACTO_LOGO_ICON), 
                            texto="Descargar CV", 
                            href=INFORMACION_PERSONAL["personal"]["CV"],
                        ),
                        spacing="0",         
                        align_items="start",
                    ),
                    align_items="center", 
                    width="100%",
                ),
                class_name=CONTACTO_CARD_BASE,
            ),
            class_name=CONTACTO_BODY_BASE
        ),
        class_name=BODY,
    )
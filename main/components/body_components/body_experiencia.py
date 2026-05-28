import reflex as rx
import json

from pathlib import Path
from ..style import (
    BODY, 
    EXPERIENCIA_HEADER_BASE, 
    EXPERIENCIA_HEADER_TITULO_PRINCIPAL,
    EXPERIENCIA_BODY_BASE, 
    EXPERIENCIA_CARD_BASE, 
    EXPERIENCIA_CARD_HEADER_BASE,
    EXPERIENCIA_CARD_HEADER_TITULO_BOX,
    EXPERIENCIA_CARD_HEADER_TITULO_TEXT,
    EXPERIENCIA_CARD_HEADER_SUBTITULO_TEXT,
    EXPERIENCIA_CARD_HEADER_FECHA_BOX,
    EXPERIENCIA_CARD_HEADER_FECHA_TEXT,
    EXPERIENCIA_CARD_BODY_BASE,
    EXPERIENCIA_CARD_BODY_DESCRIPCION_BOX,
    EXPERIENCIA_CARD_BODY_DESCRIPCION_LISTA,
    EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_BOX,
    EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG,
    EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_ZOOM,
    EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_ZOOM_CERRAR,
)


RUTA_JSON = Path(__file__).resolve().parent.parent.parent / "information" / "informacion_experiencia.json"
with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
    INFORMACION_EXPERIENCIA = json.load(archivo)



def body_experiencia() -> rx.Component:
    return rx.box(
        rx.vstack(
            # HEADER  
            rx.box(
                rx.heading("EXPERIENCIA LABORAL", class_name=EXPERIENCIA_HEADER_TITULO_PRINCIPAL), 
                class_name=EXPERIENCIA_HEADER_BASE,
            ),
            # BODY
            rx.box(
                # ============================================================================================================================
                # ====== TARJETA 1 ====== FACTORY AI ========
                rx.box(
                    # CABECERA TARJETA
                    rx.box(
                        rx.box(
                            # Títulos & Subtitulo
                            rx.vstack(
                                rx.text(INFORMACION_EXPERIENCIA["experiencia_1"]["titulo"], class_name=EXPERIENCIA_CARD_HEADER_TITULO_TEXT),
                                rx.text(INFORMACION_EXPERIENCIA["experiencia_1"]["subtitulo"], class_name=EXPERIENCIA_CARD_HEADER_SUBTITULO_TEXT),
                                spacing="1", 
                                align_items="start",
                            ),
                            class_name=EXPERIENCIA_CARD_HEADER_TITULO_BOX,
                        ),
                        rx.box(
                            # Fecha
                            rx.text(INFORMACION_EXPERIENCIA["experiencia_1"]["fecha_inicio"], class_name=EXPERIENCIA_CARD_HEADER_FECHA_TEXT),
                            rx.text(INFORMACION_EXPERIENCIA["experiencia_1"]["fecha_fin"], class_name=EXPERIENCIA_CARD_HEADER_FECHA_TEXT),
                            class_name=EXPERIENCIA_CARD_HEADER_FECHA_BOX,
                        ),
                        class_name=EXPERIENCIA_CARD_HEADER_BASE,
                    ),
                    # CUERPO TARJETA
                    rx.box(
                        # Descripcion
                        rx.box(
                            rx.unordered_list(
                                *[
                                    rx.list_item(punto) 
                                    for punto in INFORMACION_EXPERIENCIA["experiencia_1"]["descripcion"]
                                ],
                                color="text-gray-300",
                                class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_LISTA
                            ),
                            class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_BOX,
                        ),
                        # Imagen 
                        rx.box(
                            rx.dialog.root(
                                rx.dialog.trigger(
                                    rx.image(
                                        src=INFORMACION_EXPERIENCIA["experiencia_1"]["imagen"], 
                                        class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG,
                                    ),
                                ),
                                rx.dialog.content(
                                    rx.vstack(
                                        rx.image(
                                            src=INFORMACION_EXPERIENCIA["experiencia_1"]["imagen"],
                                            class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_ZOOM
                                        ),
                                        rx.dialog.close(
                                            rx.button(
                                                "Cerrar", 
                                                class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_ZOOM_CERRAR
                                            )
                                        ),
                                        align_items="center",
                                        spacing="0"
                                       ),
                                       background_color="#0E151F",
                                       border="2px solid #00D1B3",
                                       max_width="7xl",
                                       class_name="rounded-xl shadow-2xl p-4"
                                ),
                            ),
                            class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_BOX,
                        ),
                        class_name=EXPERIENCIA_CARD_BODY_BASE,
                    ),
                    class_name=EXPERIENCIA_CARD_BASE,
                ),
                # ============================================================================================================================

                # ============================================================================================================================
                # ====== TARJETA 2 ====== COOPEUCH =======
                rx.box(
                    # CABECERA TARJETA
                    rx.box(
                        rx.box(
                            # Títulos & Subtitulo
                            rx.vstack(
                                rx.text(INFORMACION_EXPERIENCIA["experiencia_2"]["titulo"], class_name=EXPERIENCIA_CARD_HEADER_TITULO_TEXT),
                                rx.text(INFORMACION_EXPERIENCIA["experiencia_2"]["subtitulo"], class_name=EXPERIENCIA_CARD_HEADER_SUBTITULO_TEXT),
                                spacing="1", 
                                align_items="start",
                            ),
                            class_name=EXPERIENCIA_CARD_HEADER_TITULO_BOX,
                        ),
                        rx.box(
                            # Fecha
                            rx.text(INFORMACION_EXPERIENCIA["experiencia_2"]["fecha_inicio"], class_name=EXPERIENCIA_CARD_HEADER_FECHA_TEXT),
                            rx.text(INFORMACION_EXPERIENCIA["experiencia_2"]["fecha_fin"], class_name=EXPERIENCIA_CARD_HEADER_FECHA_TEXT),
                            class_name=EXPERIENCIA_CARD_HEADER_FECHA_BOX,
                        ),
                        class_name=EXPERIENCIA_CARD_HEADER_BASE,
                    ),
                    # CUERPO TARJETA
                    rx.box(
                        # Descripcion
                        rx.box(
                            rx.unordered_list(
                                *[
                                    rx.list_item(punto) 
                                    for punto in INFORMACION_EXPERIENCIA["experiencia_2"]["descripcion"]
                                ],
                                color="text-gray-300",
                                class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_LISTA
                            ),
                            class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_BOX,
                        ),
                        # Imagen 
                        rx.box(
                            rx.dialog.root(
                                rx.dialog.trigger(
                                    rx.image(
                                        src=INFORMACION_EXPERIENCIA["experiencia_2"]["imagen"], 
                                        class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG,
                                    ),
                                ),
                                rx.dialog.content(
                                    rx.vstack(
                                        rx.image(
                                            src=INFORMACION_EXPERIENCIA["experiencia_2"]["imagen"],
                                            class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_ZOOM
                                        ),
                                        rx.dialog.close(
                                            rx.button(
                                                "Cerrar", 
                                                class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_ZOOM_CERRAR
                                            )
                                        ),
                                        align_items="center",
                                        spacing="0"
                                       ),
                                       background_color="#0E151F",
                                       border="2px solid #00D1B3",
                                       max_width="4xl",
                                       class_name="rounded-xl shadow-2xl p-4"
                                ),
                            ),
                            class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_BOX,
                        ),
                        class_name=EXPERIENCIA_CARD_BODY_BASE,
                    ),
                    class_name=EXPERIENCIA_CARD_BASE,
                ),
                # ============================================================================================================================

                # ============================================================================================================================
                # ====== TARJETA 3 ====== TRANSELEC
                rx.box(
                    # CABECERA TARJETA
                    rx.box(
                        rx.box(
                            # Títulos & Subtitulo
                            rx.vstack(
                                rx.text(INFORMACION_EXPERIENCIA["experiencia_3"]["titulo"], class_name=EXPERIENCIA_CARD_HEADER_TITULO_TEXT),
                                rx.text(INFORMACION_EXPERIENCIA["experiencia_3"]["subtitulo"], class_name=EXPERIENCIA_CARD_HEADER_SUBTITULO_TEXT),
                                spacing="1", 
                                align_items="start",
                            ),
                            class_name=EXPERIENCIA_CARD_HEADER_TITULO_BOX,
                        ),
                        rx.box(
                            # Fecha
                            rx.text(INFORMACION_EXPERIENCIA["experiencia_3"]["fecha_inicio"], class_name=EXPERIENCIA_CARD_HEADER_FECHA_TEXT),
                            rx.text(INFORMACION_EXPERIENCIA["experiencia_3"]["fecha_fin"], class_name=EXPERIENCIA_CARD_HEADER_FECHA_TEXT),
                            class_name=EXPERIENCIA_CARD_HEADER_FECHA_BOX,
                        ),
                        class_name=EXPERIENCIA_CARD_HEADER_BASE,
                    ),
                    # CUERPO TARJETA
                    rx.box(
                        # Descripcion
                        rx.box(
                            rx.unordered_list(
                                *[
                                    rx.list_item(punto) 
                                    for punto in INFORMACION_EXPERIENCIA["experiencia_3"]["descripcion"]
                                ],
                                color="text-gray-300",
                                class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_LISTA
                            ),
                            class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_BOX,
                        ),
                        # Imagen 
                        rx.box(
                            rx.dialog.root(
                                rx.dialog.trigger(
                                    rx.image(
                                        src=INFORMACION_EXPERIENCIA["experiencia_3"]["imagen"], 
                                        class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG,
                                    ),
                                ),
                                rx.dialog.content(
                                    rx.vstack(
                                        rx.image(
                                            src=INFORMACION_EXPERIENCIA["experiencia_3"]["imagen"],
                                            class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_ZOOM
                                        ),
                                        rx.dialog.close(
                                            rx.button(
                                                "Cerrar", 
                                                class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_ZOOM_CERRAR
                                            )
                                        ),
                                        align_items="center",
                                        spacing="0"
                                       ),
                                       background_color="#0E151F",
                                       border="2px solid #00D1B3",
                                       max_width="4xl",
                                       class_name="rounded-xl shadow-2xl p-4"
                                ),
                            ),
                            class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_BOX,
                        ),
                        class_name=EXPERIENCIA_CARD_BODY_BASE,
                    ),
                    class_name=EXPERIENCIA_CARD_BASE,
                ),
                # ============================================================================================================================

                # ============================================================================================================================
                # ====== TARJETA 4 ====== FREELANCE ======
                rx.box(
                    # CABECERA TARJETA
                    rx.box(
                        rx.box(
                            # Títulos & Subtitulo
                            rx.vstack(
                                rx.text(INFORMACION_EXPERIENCIA["experiencia_4"]["titulo"], class_name=EXPERIENCIA_CARD_HEADER_TITULO_TEXT),
                                rx.text(INFORMACION_EXPERIENCIA["experiencia_4"]["subtitulo"], class_name=EXPERIENCIA_CARD_HEADER_SUBTITULO_TEXT),
                                spacing="1", 
                                align_items="start",
                            ),
                            class_name=EXPERIENCIA_CARD_HEADER_TITULO_BOX,
                        ),
                        rx.box(
                            # Fecha
                            rx.text(INFORMACION_EXPERIENCIA["experiencia_4"]["fecha_inicio"], class_name=EXPERIENCIA_CARD_HEADER_FECHA_TEXT),
                            rx.text(INFORMACION_EXPERIENCIA["experiencia_4"]["fecha_fin"], class_name=EXPERIENCIA_CARD_HEADER_FECHA_TEXT),
                            class_name=EXPERIENCIA_CARD_HEADER_FECHA_BOX,
                        ),
                        class_name=EXPERIENCIA_CARD_HEADER_BASE,
                    ),
                    # CUERPO TARJETA
                    rx.box(
                        # Descripcion
                        rx.box(
                            rx.unordered_list(
                                *[
                                    rx.list_item(punto) 
                                    for punto in INFORMACION_EXPERIENCIA["experiencia_4"]["descripcion"]
                                ],
                                color="text-gray-300",
                                class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_LISTA
                            ),
                            class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_BOX,
                        ),
                        # Imagen 
                        rx.box(
                            rx.dialog.root(
                                rx.dialog.trigger(
                                    rx.image(
                                        src=INFORMACION_EXPERIENCIA["experiencia_4"]["imagen"], 
                                        class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG,
                                    ),
                                ),
                                rx.dialog.content(
                                    rx.vstack(
                                        rx.image(
                                            src=INFORMACION_EXPERIENCIA["experiencia_4"]["imagen"], 
                                            class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_ZOOM
                                        ),
                                        rx.dialog.close(
                                            rx.button(
                                                "Cerrar", 
                                                class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_ZOOM_CERRAR
                                            )
                                        ),
                                        align_items="center",
                                        spacing="0"
                                       ),
                                       background_color="#0E151F",
                                       border="2px solid #00D1B3",
                                       max_width="4xl",
                                       class_name="rounded-xl shadow-2xl p-4"
                                ),
                            ),
                            class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_BOX,
                        ),
                        class_name=EXPERIENCIA_CARD_BODY_BASE,
                    ),
                    class_name=EXPERIENCIA_CARD_BASE,
                ),
                # ============================================================================================================================

                # ============================================================================================================================
                # ====== TARJETA 5 ====== ZEPEDA ========
                rx.box(
                    # CABECERA TARJETA
                    rx.box(
                        rx.box(
                            # Títulos & Subtitulo
                            rx.vstack(
                                rx.text(INFORMACION_EXPERIENCIA["experiencia_5"]["titulo"], class_name=EXPERIENCIA_CARD_HEADER_TITULO_TEXT),
                                rx.text(INFORMACION_EXPERIENCIA["experiencia_5"]["subtitulo"], class_name=EXPERIENCIA_CARD_HEADER_SUBTITULO_TEXT),
                                spacing="1", 
                                align_items="start",
                            ),
                            class_name=EXPERIENCIA_CARD_HEADER_TITULO_BOX,
                        ),
                        rx.box(
                            # Fecha
                            rx.text(INFORMACION_EXPERIENCIA["experiencia_5"]["fecha_inicio"], class_name=EXPERIENCIA_CARD_HEADER_FECHA_TEXT),
                            rx.text(INFORMACION_EXPERIENCIA["experiencia_5"]["fecha_fin"], class_name=EXPERIENCIA_CARD_HEADER_FECHA_TEXT),
                            class_name=EXPERIENCIA_CARD_HEADER_FECHA_BOX,
                        ),
                        class_name=EXPERIENCIA_CARD_HEADER_BASE,
                    ),
                    # CUERPO TARJETA
                    rx.box(
                        # Descripcion
                        rx.box(
                            rx.unordered_list(
                                *[
                                    rx.list_item(punto) 
                                    for punto in INFORMACION_EXPERIENCIA["experiencia_5"]["descripcion"]
                                ],
                                class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_LISTA
                            ),
                            class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_BOX,
                        ),
                        # Imagen 
                        rx.box(
                            rx.dialog.root(
                                rx.dialog.trigger(
                                    rx.image(
                                        src=INFORMACION_EXPERIENCIA["experiencia_5"]["imagen"],
                                        class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG,
                                    ),
                                ),
                                rx.dialog.content(
                                    rx.vstack(
                                        rx.image(
                                            src=INFORMACION_EXPERIENCIA["experiencia_5"]["imagen"],
                                            class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_ZOOM
                                        ),
                                        rx.dialog.close(
                                            rx.button(
                                                "Cerrar", 
                                                class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_ZOOM_CERRAR
                                            )
                                        ),
                                        align_items="center",
                                        spacing="0"
                                       ),
                                       background_color="#0E151F",
                                       border="2px solid #00D1B3",
                                       max_width="4xl",
                                       class_name="rounded-xl shadow-2xl p-4"
                                ),
                            ),
                            class_name=EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_BOX,
                        ),
                        class_name=EXPERIENCIA_CARD_BODY_BASE,
                    ),
                    class_name=EXPERIENCIA_CARD_BASE,
                ),
                # ============================================================================================================================

                class_name=EXPERIENCIA_BODY_BASE,
            ),
            spacing="0",
            width="100%",
        ),
        class_name=BODY,
    )
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
    ESTUDIOS_CARD_ROW_BOX,
    ESTUDIOS_CARD_ROW_TITULO_INST_BOX,
    ESTUDIOS_CARD_ROW_LINK_CERT_BOX,
    ESTUDIOS_CARD_ROW_FECHA_BOX,
    ESTUDIOS_CARD_ROW_FECHA_TEXT,
    ESTUDIOS_CARD_ROW_TITULO_INST_TEXT,
    ESTUDIOS_CARD_ROW_LINK_CERT_ICON,
)


RUTA_JSON = Path(__file__).resolve().parent.parent.parent / "information" / "informacion_estudios.json"
with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
    INFORMACION_ESTUDIOS = json.load(archivo)


def body_estudios() -> rx.Component:
    return rx.box(
        rx.vstack(
            # ==========================================
            # 1. HEADER GENERAL DE LA PÁGINA
            # ==========================================
            rx.box(
                rx.heading("ESTUDIOS", class_name=ESTUDIOS_HEADER_TITULO_PRINCIPAL),
                class_name=ESTUDIOS_HEADER_BASE,
            ),
            
            # ==========================================
            # 2. CONTENEDOR PRINCIPAL DE TARJETAS (BODY BASE)
            # ==========================================
            rx.box(

                # *******************************************************
                # ====== TARJETA 1 ====== Formacion Universitaria =======
                # *******************************************************
                rx.box(
                    # CABECERA TARJETA - GRUPO ESTUDIOS
                    rx.box(
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["grupo1"]["titulo"], class_name=ESTUDIOS_CARD_HEADER_GRUPO_TITULO_TEXT),
                            class_name=ESTUDIOS_CARD_HEADER_GRUPO_TITULO,
                        ),
                        class_name=ESTUDIOS_CARD_HEADER_GRUPO_BOX,
                    ),

                    # CELDAS TARJETA - ESTUDIO 1
                    rx.box(
                        # Fecha
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_1_1"]["fecha_inicio"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_1_1"]["fecha_fin"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_FECHA_BOX,
                        ),
                        # Titulo & Institucion
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_1_1"]["titulo"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_1_1"]["institucion"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_TITULO_INST_BOX,
                        ),
                        # LINK CERTIFICADO
                        rx.box(
                            rx.link(
                                # rx.icon("file-badge", href=INFORMACION_ESTUDIOS["estudio_1_1"]["link_certificado"], class_name=ESTUDIOS_CARD_ROW_LINK_CERT_ICON),
                                is_external=True
                            ),
                            class_name=ESTUDIOS_CARD_ROW_LINK_CERT_BOX,
                        ),
                        class_name=ESTUDIOS_CARD_ROW_BOX,
                    ),
                    # CELDAS TARJETA - ESTUDIO 2
                    rx.box(
                        # Fecha
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_1_2"]["fecha_inicio"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_1_2"]["fecha_fin"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_FECHA_BOX,
                        ),
                        # Titulo & Institucion
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_1_2"]["titulo"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_1_2"]["institucion"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_TITULO_INST_BOX,
                        ),
                        # LINK CERTIFICADO
                        rx.box(
                            rx.link(
                                rx.icon("file-badge", class_name=ESTUDIOS_CARD_ROW_LINK_CERT_ICON),
                                href=INFORMACION_ESTUDIOS["estudio_1_2"]["link_certificado"],
                                is_external=True
                            ),
                            class_name=ESTUDIOS_CARD_ROW_LINK_CERT_BOX,
                        ),
                        class_name=ESTUDIOS_CARD_ROW_BOX,
                    ),
                    # CELDAS TARJETA - ESTUDIO 3
                    rx.box(
                        # Fecha
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_1_3"]["fecha_inicio"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_1_3"]["fecha_fin"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_FECHA_BOX,
                        ),
                        # Titulo & Institucion
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_1_3"]["titulo"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_1_3"]["institucion"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_TITULO_INST_BOX,
                        ),
                        # LINK CERTIFICADO
                        rx.box(
                            rx.link(
                                rx.icon("file-badge",class_name=ESTUDIOS_CARD_ROW_LINK_CERT_ICON),
                                href=INFORMACION_ESTUDIOS["estudio_1_3"]["link_certificado"],
                                is_external=True
                            ),
                            class_name=ESTUDIOS_CARD_ROW_LINK_CERT_BOX,
                        ),
                        class_name=ESTUDIOS_CARD_ROW_BOX,
                    ),
                    class_name=ESTUDIOS_CARD_BASE,
                ),

                # ******************************************************
                # ====== TARJETA 2 ====== Certificaciones & Cursos =====
                # ******************************************************
                rx.box(
                    # CABECERA TARJETA - GRUPO ESTUDIOS
                    rx.box(
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["grupo2"]["titulo"], class_name=ESTUDIOS_CARD_HEADER_GRUPO_TITULO_TEXT),
                            class_name=ESTUDIOS_CARD_HEADER_GRUPO_TITULO,
                        ),
                        class_name=ESTUDIOS_CARD_HEADER_GRUPO_BOX,
                    ),

                    # CELDAS TARJETA - ESTUDIO 1
                    rx.box(
                        # Fecha
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_1"]["fecha_inicio"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_1"]["fecha_fin"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_FECHA_BOX,
                        ),
                        # Titulo & Institucion
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_1"]["titulo"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_1"]["institucion"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_TITULO_INST_BOX,
                        ),
                        # LINK CERTIFICADO
                        rx.box(
                            rx.link(
                                rx.icon("file-badge", class_name=ESTUDIOS_CARD_ROW_LINK_CERT_ICON),
                                href=INFORMACION_ESTUDIOS["estudio_2_1"]["link_certificado"],
                                is_external=True
                            ),
                            class_name=ESTUDIOS_CARD_ROW_LINK_CERT_BOX,
                        ),
                        class_name=ESTUDIOS_CARD_ROW_BOX,
                    ),
                    # CELDAS TARJETA - ESTUDIO 2
                    rx.box(
                        # Fecha
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_2"]["fecha_inicio"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_2"]["fecha_fin"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_FECHA_BOX,
                        ),
                        # Titulo & Institucion
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_2"]["titulo"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_2"]["institucion"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_TITULO_INST_BOX,
                        ),
                        # LINK CERTIFICADO
                        rx.box(
                            rx.link(
                                rx.icon("file-badge", class_name=ESTUDIOS_CARD_ROW_LINK_CERT_ICON),
                                href=INFORMACION_ESTUDIOS["estudio_2_2"]["link_certificado1"],
                                is_external=True
                            ),
                            rx.link(
                                rx.icon("file-badge", class_name=ESTUDIOS_CARD_ROW_LINK_CERT_ICON),
                                href=INFORMACION_ESTUDIOS["estudio_2_2"]["link_certificado2"],
                                is_external=True
                            ),
                            class_name=ESTUDIOS_CARD_ROW_LINK_CERT_BOX,
                        ),
                        class_name=ESTUDIOS_CARD_ROW_BOX,
                    ),
                    # CELDAS TARJETA - ESTUDIO 3
                    rx.box(
                        # Fecha
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_3"]["fecha_inicio"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_3"]["fecha_fin"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_FECHA_BOX,
                        ),
                        # Titulo & Institucion
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_3"]["titulo"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_3"]["institucion"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_TITULO_INST_BOX,
                        ),
                        # LINK CERTIFICADO
                        rx.box(
                            rx.link(
                                rx.icon("file-badge", class_name=ESTUDIOS_CARD_ROW_LINK_CERT_ICON),
                                href=INFORMACION_ESTUDIOS["estudio_2_3"]["link_certificado1"],
                                is_external=True
                            ),
                            rx.link(
                                rx.icon("file-badge", class_name=ESTUDIOS_CARD_ROW_LINK_CERT_ICON),
                                href=INFORMACION_ESTUDIOS["estudio_2_3"]["link_certificado2"],
                                is_external=True
                            ),
                            rx.link(
                                rx.icon("file-badge", class_name=ESTUDIOS_CARD_ROW_LINK_CERT_ICON),
                                href=INFORMACION_ESTUDIOS["estudio_2_3"]["link_certificado3"],
                                is_external=True
                            ),
                            class_name=ESTUDIOS_CARD_ROW_LINK_CERT_BOX,
                        ),
                        class_name=ESTUDIOS_CARD_ROW_BOX,
                    ),
                    
                    # CELDAS TARJETA - ESTUDIO 4
                    rx.box(
                        # Fecha
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_4"]["fecha_inicio"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_4"]["fecha_fin"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_FECHA_BOX,
                        ),
                        # Titulo & Institucion
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_4"]["titulo"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_4"]["institucion"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_TITULO_INST_BOX,
                        ),
                        # LINK CERTIFICADO
                        rx.box(
                            rx.link(
                                rx.icon("file-badge", class_name=ESTUDIOS_CARD_ROW_LINK_CERT_ICON),
                                 href=INFORMACION_ESTUDIOS["estudio_2_4"]["link_certificado"],
                                is_external=True
                            ),
                            class_name=ESTUDIOS_CARD_ROW_LINK_CERT_BOX,
                        ),
                        class_name=ESTUDIOS_CARD_ROW_BOX,
                    ),

                    # CELDAS TARJETA - ESTUDIO 5
                    rx.box(
                        # Fecha
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_5"]["fecha_inicio"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_5"]["fecha_fin"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_FECHA_BOX,
                        ),
                        # Titulo & Institucion
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_5"]["titulo"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_5"]["institucion"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_TITULO_INST_BOX,
                        ),
                        # LINK CERTIFICADO
                        rx.box(
                            rx.link(
                                rx.icon("file-badge", class_name=ESTUDIOS_CARD_ROW_LINK_CERT_ICON),
                                href=INFORMACION_ESTUDIOS["estudio_2_5"]["link_certificado"],
                                is_external=True
                            ),
                            class_name=ESTUDIOS_CARD_ROW_LINK_CERT_BOX,
                        ),
                        class_name=ESTUDIOS_CARD_ROW_BOX,
                    ),
                    # CELDAS TARJETA - ESTUDIO 5
                    rx.box(
                        # Fecha
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_6"]["fecha_inicio"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_6"]["fecha_fin"], class_name=ESTUDIOS_CARD_ROW_FECHA_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_FECHA_BOX,
                        ),
                        # Titulo & Institucion
                        rx.box(
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_6"]["titulo"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            rx.text(INFORMACION_ESTUDIOS["estudio_2_6"]["institucion"], class_name=ESTUDIOS_CARD_ROW_TITULO_INST_TEXT),
                            class_name=ESTUDIOS_CARD_ROW_TITULO_INST_BOX,
                        ),
                        # LINK CERTIFICADO
                        rx.box(
                            rx.link(
                                rx.icon("file-badge", class_name=ESTUDIOS_CARD_ROW_LINK_CERT_ICON),
                                href=INFORMACION_ESTUDIOS["estudio_2_6"]["link_certificado"],
                                is_external=True
                            ),
                            class_name=ESTUDIOS_CARD_ROW_LINK_CERT_BOX,
                        ),
                        class_name=ESTUDIOS_CARD_ROW_BOX,
                    ),
                    class_name=ESTUDIOS_CARD_BASE,
                ),
                class_name=ESTUDIOS_BODY_BASE,
            ),
            spacing="0",
            width="100%",
        ),
        class_name=BODY,
    )
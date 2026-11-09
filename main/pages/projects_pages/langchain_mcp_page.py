import reflex as rx

from main.components.body_components.body_project_Langchain import (
    INFORMACION_PROYECTOS,
    card_proyecto as card_proyecto_langchain,
)
from main.components.body_components.body_project_mcp import (
    card_proyecto as card_proyecto_mcp,
)

from ...components.background import neural_background
from ...components.navbar import navbar
from ...components.footer import footer
from ...components.style import (
    BODY,
    PROYECTOS_HEADER_BASE,
    PROYECTOS_HEADER_TITULO_PRINCIPAL,
    PROYECTOS_BODY_BASE,
)


def proyectos_langchain_mcp_page() -> rx.Component:
    return rx.vstack(
        neural_background(),

        navbar(),

        rx.box(
            rx.vstack(
                rx.box(
                    rx.heading(
                        "PROYECTOS LANGCHAIN & MCP",
                        class_name=PROYECTOS_HEADER_TITULO_PRINCIPAL,
                    ),
                    class_name=PROYECTOS_HEADER_BASE,
                ),
                rx.box(
                    rx.vstack(
                        card_proyecto_langchain(
                            INFORMACION_PROYECTOS["proyecto_langchain_1"]
                        ),
                        card_proyecto_mcp(
                            INFORMACION_PROYECTOS["proyecto_mcp_1"]
                        ),
                        spacing="8",
                        width="100%",
                        align_items="center",
                    ),
                    class_name=PROYECTOS_BODY_BASE,
                ),
                spacing="0",
                width="100%",
            ),
            class_name=BODY,
        ),

        footer(),

        bg="#0E151F",
        width="100%",
        min_height="100vh",
        font_family="system-ui, sans-serif",
        spacing="0",
    )

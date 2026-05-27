import reflex as rx

from ..components.style import (FOOTER_BASE, FOOTER_TEXT)

def footer() -> rx.Component:
    return rx.box(
        rx.text(
            "Desarrollado por: Diego Videla Silva",
            class_name=FOOTER_TEXT
        ),
        rx.text(
            "© 2026. Todos los derechos reservados.",
            class_name=FOOTER_TEXT
        ),
        class_name=FOOTER_BASE,
    )
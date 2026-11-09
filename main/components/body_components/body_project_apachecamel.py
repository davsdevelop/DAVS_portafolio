import reflex as rx

from ..style import (
    BODY,
    PROYECTOS_HEADER_BASE,
    PROYECTOS_HEADER_TITULO_PRINCIPAL,
    PROYECTOS_BODY_BASE,
)


def proyectos_apachecamel() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.heading(
                    "PROYECTOS APACHE CAMEL - FUSE",
                    class_name=PROYECTOS_HEADER_TITULO_PRINCIPAL,
                ),
                class_name=PROYECTOS_HEADER_BASE,
            ),
            rx.box(
                rx.box(
                    rx.vstack(
                        rx.icon(
                            tag="wrench",
                            size=42,
                            class_name="text-davs-color-cian",
                        ),
                        rx.text(
                            "EN MANTENCION",
                            class_name=(
                                "text-davs-color-blanco text-2xl md:text-3xl "
                                "font-bold tracking-widest text-center"
                            ),
                        ),
                        spacing="4",
                        align_items="center",
                        justify_content="center",
                    ),
                    class_name=(
                        "w-full max-w-3xl min-h-[300px] bg-[#0E151F] "
                        "rounded-xl border border-[#1E293B] shadow-lg "
                        "flex justify-center items-center p-8"
                    ),
                ),
                class_name=PROYECTOS_BODY_BASE,
            ),
            spacing="0",
            width="100%",
        ),
        class_name=BODY,
    )

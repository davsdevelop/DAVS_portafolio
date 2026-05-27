import reflex as rx

from ..components.style import (
    NAVBAR_BASE, 
    NAVBAR_LOGO_IMG, 
    NAVBAR_LINK, 
    NAVBAR_LINK_TEXT, 
    NAVBAR_ELEMENTOS_INTERIOR,
    NAVBAR_MENU_ITEM, 
    NAVBAR_MENU_LINK  
)

def navbar(show_home: bool = True) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image("/davs/DAVS_cian.png", class_name=NAVBAR_LOGO_IMG),
            rx.box(class_name="flex-1"),
            # --- LINK HOME ---
            rx.cond(
                show_home,
                rx.hstack(
                    rx.text("00.", class_name=NAVBAR_LINK_TEXT),
                    rx.link("Home", href="/", class_name=NAVBAR_LINK),
                    align_items="center",
                    spacing="1",
                ),
            ),
            # --- LINK EXPERIENCIA ---
            rx.hstack(   
                rx.text("01.", class_name=NAVBAR_LINK_TEXT),
                rx.link("Experiencia", href="/experiencia", class_name=NAVBAR_LINK), 
                align_items="center",
                spacing="1",
            ),
            # --- LINK ESTUDIOS ---
            rx.hstack(   
                rx.text("02.", class_name=NAVBAR_LINK_TEXT),
                rx.link("Estudios", href="/estudios", class_name=NAVBAR_LINK),
                align_items="center",
                spacing="1",
            ),
            # --- LINK PROYECTOS --- MENÚ DESPLEGABLE DE PROYECTOS ---
            rx.menu.root(
                rx.menu.trigger(
                    rx.hstack(   
                        rx.text("03.", class_name=NAVBAR_LINK_TEXT),
                        rx.text("Proyectos", class_name=NAVBAR_LINK),
                        align_items="center",
                        spacing="1",
                    ),
                ),
                rx.menu.content(
                    rx.menu.item(
                        rx.link("Python", href="/proyectospython", width="100%", display="block", _hover={"text_decoration": "none"}, class_name=NAVBAR_MENU_LINK), 
                        class_name=NAVBAR_MENU_ITEM
                    ),
                    rx.menu.item(
                        rx.link("FastAPI", href="/proyectosfastapi", width="100%", display="block", _hover={"text_decoration": "none"}, class_name=NAVBAR_MENU_LINK), 
                        class_name=NAVBAR_MENU_ITEM
                    ),
                    rx.menu.item(
                        rx.link("Django", href="/proyectosdjango", width="100%", display="block", _hover={"text_decoration": "none"}, class_name=NAVBAR_MENU_LINK), 
                        class_name=NAVBAR_MENU_ITEM
                    ),
                    rx.menu.item(
                        rx.link("Reflex", href="/proyectosreflex", width="100%", display="block", _hover={"text_decoration": "none"}, class_name=NAVBAR_MENU_LINK), 
                        class_name=NAVBAR_MENU_ITEM
                    ),
                    rx.menu.item(
                        rx.link("SQL", href="/proyectossql", width="100%", display="block", _hover={"text_decoration": "none"}, class_name=NAVBAR_MENU_LINK), 
                        class_name=NAVBAR_MENU_ITEM
                    ),
                    bg="#0a0f16", 
                    border="1px solid #00D1B3", 
                    border_radius="8px",
                    padding="8px",
                ),
            ),
            # --- LINK CONTACTO ---
            rx.hstack(   
                rx.text("04.", class_name=NAVBAR_LINK_TEXT),
                rx.link("Contacto", href="/contacto", class_name=NAVBAR_LINK),
                align_items="center",
                spacing="1",
            ),
            class_name=NAVBAR_ELEMENTOS_INTERIOR,
            spacing="6",
            align_items="center"
        ),
        class_name=NAVBAR_BASE
    )
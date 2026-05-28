import reflex as rx
from ..components.style import (
    NAVBAR_BASE, NAVBAR_LOGO_IMG, NAVBAR_LINK, NAVBAR_LINK_TEXT, 
    NAVBAR_ELEMENTOS_INTERIOR, NAVBAR_MENU_ITEM, NAVBAR_MENU_LINK
)

def navbar(show_home: bool = True) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image("/davs/DAVS_cian.png", class_name=NAVBAR_LOGO_IMG),
            rx.box(class_name="flex-1"),

            # --- ESCRITORIO ---
            rx.hstack(
                rx.cond(show_home, rx.hstack(rx.text("00.", class_name=NAVBAR_LINK_TEXT), rx.link("Home", href="/", class_name=NAVBAR_LINK), align_items="center", spacing="1")),
                rx.hstack(rx.text("01.", class_name=NAVBAR_LINK_TEXT), rx.link("Experiencia", href="/experiencia", class_name=NAVBAR_LINK), align_items="center", spacing="1"),
                rx.hstack(rx.text("02.", class_name=NAVBAR_LINK_TEXT), rx.link("Estudios", href="/estudios", class_name=NAVBAR_LINK), align_items="center", spacing="1"),
                
                rx.menu.root(
                    rx.menu.trigger(rx.hstack(rx.text("03.", class_name=NAVBAR_LINK_TEXT), rx.text("Proyectos", class_name=NAVBAR_LINK), align_items="center", spacing="1")),
                    rx.menu.content(
                        rx.menu.item(rx.link("Python", href="/proyectospython", class_name=NAVBAR_MENU_LINK), class_name=NAVBAR_MENU_ITEM),
                        rx.menu.item(rx.link("FastAPI", href="/proyectosfastapi", class_name=NAVBAR_MENU_LINK), class_name=NAVBAR_MENU_ITEM),
                        rx.menu.item(rx.link("Django", href="/proyectosdjango", class_name=NAVBAR_MENU_LINK), class_name=NAVBAR_MENU_ITEM),
                        rx.menu.item(rx.link("Reflex", href="/proyectosreflex", class_name=NAVBAR_MENU_LINK), class_name=NAVBAR_MENU_ITEM),
                        rx.menu.item(rx.link("SQL", href="/proyectossql", class_name=NAVBAR_MENU_LINK), class_name=NAVBAR_MENU_ITEM),
                        bg="#0a0f16", border="1px solid #00D1B3", border_radius="8px", padding="8px",
                    ),
                ),
                rx.hstack(rx.text("04.", class_name=NAVBAR_LINK_TEXT), rx.link("Contacto", href="/contacto", class_name=NAVBAR_LINK), align_items="center", spacing="1"),
                
                class_name="hidden md:flex", 
                spacing="6",
                align_items="center"
            ),

            # --- MÓVIL ---
            rx.box(
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30, class_name="text-davs-color-cian cursor-pointer")),
                    rx.menu.content(
                        rx.menu.item(rx.link("Home", href="/", class_name=NAVBAR_MENU_LINK), class_name=NAVBAR_MENU_ITEM),
                        rx.menu.item(rx.link("Experiencia", href="/experiencia", class_name=NAVBAR_MENU_LINK), class_name=NAVBAR_MENU_ITEM),
                        rx.menu.item(rx.link("Estudios", href="/estudios", class_name=NAVBAR_MENU_LINK), class_name=NAVBAR_MENU_ITEM),
                        rx.menu.item(rx.link("Proyectos", href="/proyectospython", class_name=NAVBAR_MENU_LINK), class_name=NAVBAR_MENU_ITEM),
                        rx.menu.item(rx.link("Contacto", href="/contacto", class_name=NAVBAR_MENU_LINK), class_name=NAVBAR_MENU_ITEM),
                        bg="#0a0f16", border="1px solid #00D1B3", border_radius="8px", padding="8px",
                    ),
                ),
                class_name="md:hidden" 
            ),
            
            class_name=NAVBAR_ELEMENTOS_INTERIOR,
            align_items="center"
        ),
        class_name=NAVBAR_BASE
    )
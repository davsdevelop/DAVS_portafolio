import reflex as rx

from ...components.background import neural_background
from ...components.navbar import navbar
from ...components.footer import footer
from ...components.body_components.body_project_python import proyectos_python


def proyectos_python_page() -> rx.Component:
    return rx.vstack(
        
        neural_background(),
        
        navbar(),

        proyectos_python(),
        
        footer(),
        
        bg="#0E151F",                           
        width="100%",
        min_height="100vh", 
        font_family="system-ui, sans-serif",
        spacing="0", 
    )

app = rx.App()
app.add_page(proyectos_python_page)
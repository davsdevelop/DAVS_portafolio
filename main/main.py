import reflex as rx

from .components.background import neural_background
from .components.navbar import navbar
from .components.footer import footer
from .components.body_components.body_home import body_home

from .pages.experiencia_page import experiencia_page
from .pages.estudios_page import estudios_page
from .pages.contacto_page import sobre_mi_page
from .pages.projects_pages.python_page import proyectos_python_page
from .pages.projects_pages.fastapi_page import proyectos_fastapi_page
from .pages.projects_pages.django_page import proyectos_django_page
from .pages.projects_pages.reflex_page import proyectos_reflex_page
from .pages.projects_pages.sql_page import proyectos_sql_page


def index() -> rx.Component:
    return rx.vstack(
        
        neural_background(),
    
        navbar(False),

        body_home(),
        
        footer(),
        
        bg="#0E151F",                           
        width="100%",
        min_height="100vh", 
        spacing="0", 
    )

app = rx.App(
    stylesheets=[
        "/custom.css"
    ]
)
app.add_page(index)

app.add_page(experiencia_page(), route="/experiencia")
app.add_page(estudios_page(), route="/estudios")
app.add_page(sobre_mi_page(), route="/contacto")
app.add_page(proyectos_python_page(), route="/proyectospython")
app.add_page(proyectos_fastapi_page(), route="/proyectosfastapi")
app.add_page(proyectos_django_page(), route="/proyectosdjango")
app.add_page(proyectos_reflex_page(), route="/proyectosreflex")
app.add_page(proyectos_sql_page(), route="/proyectossql")

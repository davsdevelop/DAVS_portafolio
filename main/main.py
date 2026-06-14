import reflex as rx

from .components.background import neural_background
from .components.navbar import navbar
from .components.footer import footer
from .components.body_components.body_home import body_home

from .pages.experiencia_page import experiencia_page
from .pages.estudios_page import estudios_page
from .pages.contacto_page import sobre_mi_page
from .pages.ml_page import ml_page
from .pages.projects_pages.python_page import proyectos_python_page
from .pages.projects_pages.fastapi_page import proyectos_fastapi_page
from .pages.projects_pages.django_page import proyectos_django_page
from .pages.projects_pages.reflex_page import proyectos_reflex_page
from .pages.projects_pages.sql_page import proyectos_sql_page


@rx.page(
    route="/", 
    title="DAVSportafolio",  
    description="Mi portafolio profesional",
)
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

app.add_page(experiencia_page(), route="/experiencia", title="DAVSportafolio | Experiencia")
app.add_page(estudios_page(), route="/estudios", title="DAVSportafolio | Estudios")
app.add_page(sobre_mi_page(), route="/contacto", title="DAVSportafolio | Contacto")
app.add_page(proyectos_python_page(), route="/proyectospython", title="DAVSportafolio | Python")
app.add_page(proyectos_fastapi_page(), route="/proyectosfastapi", title="DAVSportafolio | FastAPI")
app.add_page(proyectos_django_page(), route="/proyectosdjango", title="DAVSportafolio | Django")
app.add_page(proyectos_reflex_page(), route="/proyectosreflex", title="DAVSportafolio | Reflex")
app.add_page(proyectos_sql_page(), route="/proyectossql", title="DAVSportafolio | SQL")
app.add_page(ml_page(), route="/proyectosML", title="DAVSportafolio | Machine Learning")

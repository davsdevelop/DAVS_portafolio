import reflex as rx

from main.pages.projects_pages.langchain_page import proyectos_langchain_page
from main.pages.projects_pages.mcp_page import proyectos_mcp_page
from main.pages.projects_pages.langchain_mcp_page import proyectos_langchain_mcp_page

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
from .pages.projects_pages.nestjs_page import proyectos_nestjs_page
from .pages.projects_pages.react_page import proyectos_react_page
from .pages.projects_pages.datayml_page import proyectos_datayml_page
from .pages.projects_pages.apachecamel_page import proyectos_apachecamel_page


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

def not_found() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("404", class_name="text-davs-color-cian text-6xl font-bold"),
            rx.text(
                "Página no encontrada",
                class_name="text-davs-color-blanco text-xl md:text-2xl text-center",
            ),
            rx.link(
                "Volver al inicio",
                href="/",
                class_name="text-davs-color-cian hover:text-white transition-colors",
            ),
            spacing="4",
            align_items="center",
        ),
        width="100%",
        min_height="100vh",
        bg="#0E151F",
    )


app = rx.App(
    stylesheets=[
        "/custom.css"
    ],
    html_lang="es",
)

DESCRIPCION_SITIO = "Portafolio profesional de Diego Arturo Videla Silva."

app.add_page(experiencia_page(), route="/experiencia", title="DAVSportafolio | Experiencia", description=f"Experiencia laboral. {DESCRIPCION_SITIO}")
app.add_page(estudios_page(), route="/estudios", title="DAVSportafolio | Estudios", description=f"Estudios y certificaciones. {DESCRIPCION_SITIO}")
app.add_page(sobre_mi_page(), route="/contacto", title="DAVSportafolio | Contacto", description=f"Datos de contacto. {DESCRIPCION_SITIO}")
app.add_page(proyectos_python_page(), route="/proyectospython", title="DAVSportafolio | Python", description=f"Proyectos en Python. {DESCRIPCION_SITIO}")
app.add_page(proyectos_fastapi_page(), route="/proyectosfastapi", title="DAVSportafolio | FastAPI", description=f"Proyectos en FastAPI. {DESCRIPCION_SITIO}")
app.add_page(proyectos_django_page(), route="/proyectosdjango", title="DAVSportafolio | Django", description=f"Proyectos en Django. {DESCRIPCION_SITIO}")
app.add_page(proyectos_reflex_page(), route="/proyectosreflex", title="DAVSportafolio | Reflex", description=f"Proyectos en Reflex. {DESCRIPCION_SITIO}")
app.add_page(proyectos_sql_page(), route="/proyectossql", title="DAVSportafolio | SQL", description=f"Proyectos de datos y SQL. {DESCRIPCION_SITIO}")
app.add_page(ml_page(), route="/proyectosML", title="DAVSportafolio | Machine Learning", description=f"Machine Learning y redes neuronales. {DESCRIPCION_SITIO}")
app.add_page(proyectos_nestjs_page(), route="/proyectosnestjs", title="DAVSportafolio | NestJS", description=f"Proyectos en NestJS. {DESCRIPCION_SITIO}")
app.add_page(proyectos_react_page(), route="/proyectosreact", title="DAVSportafolio | React", description=f"Proyectos en React. {DESCRIPCION_SITIO}")
app.add_page(proyectos_datayml_page(), route="/proyectosdatayml", title="DAVSportafolio | ETL & ML", description=f"Proyectos ETL y Machine Learning. {DESCRIPCION_SITIO}")
app.add_page(proyectos_apachecamel_page(), route="/proyectosapachecamel", title="DAVSportafolio | Apache Camel - Fuse", description=f"Proyectos de integración con Apache Camel. {DESCRIPCION_SITIO}")

app.add_page(proyectos_langchain_page(), route="/proyectoslangchain", title="DAVSportafolio | LangChain", description=f"Proyectos con LangChain. {DESCRIPCION_SITIO}")
app.add_page(proyectos_mcp_page(), route="/proyectosmcp", title="DAVSportafolio | MCP", description=f"Proyectos con Model Context Protocol. {DESCRIPCION_SITIO}")
app.add_page(proyectos_langchain_mcp_page(), route="/proyectoslangchainmcp", title="DAVSportafolio | LangChain & MCP", description=f"Proyectos con LangChain y MCP. {DESCRIPCION_SITIO}")
app.add_page(not_found, route="404", title="DAVSportafolio | Página no encontrada", description=f"Página no encontrada. {DESCRIPCION_SITIO}")

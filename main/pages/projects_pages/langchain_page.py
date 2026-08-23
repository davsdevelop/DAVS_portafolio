import reflex as rx

from main.components.body_components.body_project_Langchain import proyectos_langchain

from ...components.background import neural_background
from ...components.navbar import navbar
from ...components.footer import footer



def proyectos_langchain_page() -> rx.Component:
    return rx.vstack(
        
        neural_background(),
        
        navbar(),

        proyectos_langchain(),
        
        footer(),
        
        bg="#0E151F",                           
        width="100%",
        min_height="100vh", 
        font_family="system-ui, sans-serif",
        spacing="0", 
    )

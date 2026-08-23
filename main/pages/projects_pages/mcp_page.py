import reflex as rx


from main.components.body_components.body_project_mcp import proyectos_mcp

from ...components.background import neural_background
from ...components.navbar import navbar
from ...components.footer import footer



def proyectos_mcp_page() -> rx.Component:
    return rx.vstack(
        
        neural_background(),
        
        navbar(),

        proyectos_mcp(),
        
        footer(),
        
        bg="#0E151F",                           
        width="100%",
        min_height="100vh", 
        font_family="system-ui, sans-serif",
        spacing="0", 
    )

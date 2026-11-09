import reflex as rx
from main.components.paleta_colores import mi_paleta_colores

config = rx.Config(
    app_name="main",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(config=mi_paleta_colores),
        rx.plugins.RadixThemesPlugin(),
    ]
)
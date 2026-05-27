import reflex as rx
from main.components.paleta_colores import mi_paleta_colores

config = rx.Config(
    app_name="main",
    tailwind=mi_paleta_colores,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(),
    ]
)
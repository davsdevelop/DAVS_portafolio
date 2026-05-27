# components/background.py
import reflex as rx

def neural_background() -> rx.Component:
    """
    Componente que renderiza el fondo oscuro con la red neuronal animada/estática.
    Utiliza una máscara CSS para poder inyectar el color directamente.
    """
    return rx.box(
            background_image="url('/neuronal-background.svg')",
            background_position="center",
            background_size="cover",
            background_repeat="no-repeat",
            
            opacity="0.4",  
            
            position="fixed",    # Se queda anclado a la pantalla
            top="0",             # Desde el borde superior...
            left="0",            # ...hasta el borde izquierdo
            width="100vw",       # 100% del ancho de la ventana
            height="100vh",      # 100% del alto de la ventana
            z_index="0",         # Lo mandamos al fondo de todo     
    )
# ==========================================
# NAVBAR STYLES
# ==========================================
NAVBAR_BASE = "w-full h-[70px] bg-davs-color-base sticky top-0 z-50"
NAVBAR_LOGO_IMG = "h-[55px] w-auto ml-4 mt-2 object-contain"
NAVBAR_LINK = "text-davs-color-morado-claro hover:!text-davs-color-morado-oscuro transition-colors cursor-pointer"
NAVBAR_LINK_TEXT = "text-davs-color-cian"
NAVBAR_ELEMENTOS_INTERIOR = "px-6 md:pr-14 w-full flex justify-between items-center"
NAVBAR_MENU_ITEM = "group hover:bg-[#0E151F] cursor-pointer"
NAVBAR_MENU_LINK = "!text-davs-color-morado-claro group-hover:!text-davs-color-cian transition-colors"


# ==========================================
# BODY STYLES
# ==========================================
BODY = "flex-1 w-full relative z-10 overflow-x-hidden"
GRID_3_COLS = "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 w-full gap-10 md:gap-0"

COL_SPAN_1 = "col-span-1 flex h-full w-full items-center justify-center"
COL_SPAN_2 = "col-span-1 md:col-span-2 lg:col-span-2 flex h-full w-full items-center justify-center"


# ==========================================
# HOME - PRESENTACION STYLES
# ==========================================
BODY_HOME_PRESENTACION_BASE = "h-auto min-h-[450px] w-full max-w-[650px] mr-0 px-6 md:px-0 mt-8 md:mt-0"
BODY_HOME_PRESENTACION_FOTO_BASE = (
    "h-[180px] w-[180px] md:h-[250px] md:w-[250px] "
    "rounded-full "               
    "border-2 border-[#00D1B3] "  
    "bg-[#0E151F] "               
    "overflow-hidden "           
    "flex justify-center items-center shrink-0" 
)
# BODY SECCION PRESENTACION
BODY_HOME_PRESENTACION_TEXTO_SALUDO = "h-auto w-full max-w-[400px] flex flex-col justify-end items-center md:items-start pb-1 pt-4 md:pt-0 md:pl-5 text-xl md:text-2xl text-davs-color-blanco text-center md:text-left"
BODY_HOME_PRESENTACION_TEXTO_MI_NOMBRE = "h-auto w-full max-w-[400px] flex flex-col justify-start items-center md:items-start pt-0 md:pl-5 text-2xl md:text-3xl font-bold text-davs-color-blanco text-center md:text-left"
BODY_HOME_PRESENTACION_TEXTO_CARGO = "h-auto w-full max-w-[650px] mt-6 md:mt-8 mb-4 text-davs-color-cian font-semibold tracking-widest text-sm md:text-base text-center md:text-left"
BODY_HOME_PRESENTACION_TEXTO_BIOGRAFIA = "h-auto w-full max-w-[650px] flex flex-col justify-start items-center md:items-start pb-3 md:pl-2 text-sm md:text-base text-davs-color-morado-claro text-center md:text-left"
BODY_HOME_PRESENTACION_FOTO = (
    "w-full h-full object-cover "
    "scale-[1.3]"                
)
# BODY SECCION PROYECTOS
BODY_HOME_PROYECTOS_BASE = "h-auto min-h-[650px] w-full max-w-[250px] md:mr-12 flex flex-col justify-start items-center md:items-start pt-10 pb-20 md:pb-0"  # ← CORREGIDO: mr-50 no existe en Tailwind
BODY_HOME_PROYECTOS_TITULO = "h-auto w-[250px] flex flex-col justify-start items-center mb-2 text-sm font-bold text-davs-color-morado-oscuro"
BODY_HOME_PROYECTOS_SEPARATOR = "w-full text-center text-davs-color-morado-oscuro text-lg tracking-widest"
BODY_HOME_PROYECTOS_TECH_NAME_TEXT = (
    "absolute left-[50%] ml-[55px] "
    "text-sm text-davs-color-morado-claro whitespace-nowrap "
    "opacity-0 -translate-x-4 "
    "group-hover:opacity-100 group-hover:translate-x-0 "
    "transition-all duration-300 ease-out "
    "pointer-events-none z-50 "
    "hidden md:block"                  # ← CORREGIDO: se oculta en mobile para evitar overflow
)
BODY_HOME_PROYECTOS_BASE_PROYECTOS = (
    "w-full h-auto flex flex-row justify-center items-center "
    "group pb-1 cursor-pointer " 
    "transition-all duration-300 ease-in-out"
)
BODY_HOME_PROYECTOS_BOTON_ANIMACION_BASE = (
    "h-[80px] w-[80px] rounded-full " 
    "flex justify-center items-center "
    "border-2 border-davs-color-cian " 
    "bg-davs-color-base "          
    "transition-all duration-300 ease-out "    
    "transform hover:scale-110 hover:-translate-y-2 " 
    "hover:shadow-[0_0_20px_rgba(70,172,159,0.3)] " 
    "cursor-pointer z-20"  
)
BODY_HOME_PROYECTOS_LOGO_IMG = "h-full w-full object-contain p-2" 

 
# ==========================================
# PROYECTOS STYLES 
# ==========================================
PROYECTOS_HEADER_BASE = "w-full h-[60px] flex justify-center items-center"
PROYECTOS_HEADER_TITULO_PRINCIPAL = "text-davs-color-morado-claro text-3xl font-bold " 
PROYECTOS_BODY_BASE = "w-full min-h-screen py-12 px-8 md:px-24 flex flex-col gap-8 items-center"
PROYECTOS_CARD_BASE = (
    "w-full max-w-7xl h-auto flex flex-col "
    "bg-[#0E151F] rounded-xl overflow-hidden shadow-lg "
    "border border-[#00D1B3]"   # ← era "border-1 border-[#00D1B3]"
)
PROYECTOS_CARD_BASE_TITULO = "w-full h-[50px] bg-davs-color-base px-6 flex items-center border-b border-davs-color-cian"
PROYECTOS_CARD_BASE_DESCRIPCION = "w-full flex-1 p-6"
PROYECTOS_CARD_BASE_TITULO_CONTENEDOR = "w-full min-h-[50px] h-auto bg-davs-color-base px-2 flex flex-row items-center border-b border-davs-color-cian"
PROYECTOS_CARD_TITULO_TEXTO = "w-full md:w-[80%] p-4 flex items-center font-bold text-davs-color-morado-oscuro text-xl md:text-2xl break-words"
PROYECTOS_CARD_TITULO_ICONOS = "w-full md:w-[20%] flex items-center justify-center md:justify-end gap-4 p-4"
PROYECTOS_CARD_BASE_DESCRIPCION_CONTENEDOR = "w-full flex-1 flex flex-col md:flex-row" # flex-col para móvil
PROYECTOS_CARD_DESC_TEXTO = "w-full md:w-[60%] p-6 flex flex-col justify-start text-sm md:text-base"
PROYECTOS_CARD_DESC_IMG_CAJA = "w-full md:w-[40%] h-auto p-6 flex justify-center items-center"
PROYECTOS_CARD_DESC_IMG = "w-full h-full object-cover rounded-xl border-2 border-davs-color-cian"
PROYECTOS_CARD_ICONO_LINK = "text-davs-color-cian hover:!text-white transition-colors cursor-pointer"


# ==========================================
# EXPERIENCIA STYLES 
# ==========================================
EXPERIENCIA_HEADER_BASE = "w-full h-[60px] flex justify-center items-center"
EXPERIENCIA_HEADER_TITULO_PRINCIPAL = "text-davs-color-morado-claro text-3xl font-bold"
EXPERIENCIA_BODY_BASE = "w-full min-h-screen py-12 px-8 md:px-24 grid grid-cols-1 lg:grid-cols-2 gap-8 justify-items-center items-start"
EXPERIENCIA_CARD_BASE = (
    "w-full max-w-2xl h-auto min-h-[300px] flex flex-col "
    "bg-[#0E151F] rounded-xl overflow-hidden shadow-lg "
    "border border-[#00D1B3]"
)
# ==== EXPERIENCIA CARD - HEADER
EXPERIENCIA_CARD_HEADER_BASE = "w-full h-auto min-h-[70px] bg-davs-color-base px-4 py-4 flex flex-row items-center border-b border-davs-color-cian"
EXPERIENCIA_CARD_HEADER_TITULO_BOX = "flex-1 h-auto flex flex-col justify-center"          # ← CORREGIDO: era w-[80%], suma > 100%
EXPERIENCIA_CARD_HEADER_TITULO_TEXT = "text-white font-bold"
EXPERIENCIA_CARD_HEADER_SUBTITULO_TEXT = "text-[#00D1B3] text-sm"
EXPERIENCIA_CARD_HEADER_FECHA_BOX = "w-auto h-auto flex flex-col items-end justify-center shrink-0 pl-4"  # ← CORREGIDO: era w-[25%], ahora shrink-0
EXPERIENCIA_CARD_HEADER_FECHA_TEXT = "text-white text-sm text-right"
# ==== EXPERIENCIA CARD - BODY 
EXPERIENCIA_CARD_BODY_BASE = "w-full flex-1 flex flex-col md:flex-row"                      # ← CORREGIDO: era solo flex-row, roto en mobile
EXPERIENCIA_CARD_BODY_DESCRIPCION_BOX = "w-full md:w-[60%] h-auto p-6 pb-8 flex flex-col justify-start"   # ← CORREGIDO: w-full en mobile
EXPERIENCIA_CARD_BODY_DESCRIPCION_LISTA = "list-disc ml-6 space-y-2"
EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_BOX = "w-full md:w-[40%] h-full p-4 flex justify-center items-center"  # ← CORREGIDO: w-full en mobile
EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG = "w-full h-auto object-contain rounded-lg border border-gray-700 cursor-zoom-in hover:opacity-80 transition-opacity"
EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_ZOOM = "w-full h-auto max-h-[90vh] object-contain rounded-xl"
EXPERIENCIA_CARD_BODY_DESCRIPCION_IMG_ZOOM_CERRAR = "mt-4 px-6 py-2 bg-[#0E151F] text-white border border-[#00D1B3] hover:bg-[#00D1B3] hover:text-black rounded-lg transition-colors cursor-pointer"


# ==========================================
# ESTUDIOS STYLES 
# ==========================================
ESTUDIOS_HEADER_BASE = "w-full h-[60px] flex justify-center items-center"
ESTUDIOS_HEADER_TITULO_PRINCIPAL = "text-davs-color-morado-claro text-3xl font-bold"
ESTUDIOS_BODY_BASE = "w-full min-h-screen py-2 px-8 md:px-24 flex flex-col gap-8 items-center"
ESTUDIOS_CARD_BASE = (
    "w-full max-w-3xl h-auto flex flex-col "
    "bg-[#0E151F] rounded-xl overflow-hidden shadow-lg "
    "border border-[#00D1B3]"
)
ESTUDIOS_CARD_HEADER_GRUPO_BOX = "w-full h-[50px] bg-davs-color-base px-6 flex flex-row items-center border-b border-davs-color-cian"
ESTUDIOS_CARD_HEADER_GRUPO_TITULO = "w-full h-full flex items-center p-4"
ESTUDIOS_CARD_HEADER_GRUPO_TITULO_TEXT = "text-davs-color-morado-claro font-bold text-lg"
ESTUDIOS_CARD_ROW_BOX = "w-full flex flex-row border-b border-gray-800 last:border-0"
ESTUDIOS_CARD_ROW_FECHA_BOX = "w-[15%] h-auto flex flex-col items-start justify-center pl-2"
ESTUDIOS_CARD_ROW_FECHA_TEXT = "text-white text-sm"
ESTUDIOS_CARD_ROW_TITULO_INST_BOX = "w-[75%] h-auto flex flex-col items-start justify-center pl-4"
ESTUDIOS_CARD_ROW_TITULO_INST_TEXT = "text-white text-base"
ESTUDIOS_CARD_ROW_LINK_CERT_BOX = "w-[10%] h-[100px] p-4 flex justify-center items-center"
ESTUDIOS_CARD_ROW_LINK_CERT_ICON = "text-cian-300 hover:text-white transition-colors"  # ← CORREGIDO: era "gray.300"



# ==========================================
# CONTACTO STYLES
# ==========================================
CONTACTO_BODY_BASE = "w-full h-auto py-4 px-8 md:px-24 flex flex-col gap-8 items-center justify-center"
CONTACTO_CARD_BASE = (
    "w-full max-w-xl h-auto flex flex-col justify-center items-center "
    "bg-[#0E151F] rounded-xl overflow-hidden shadow-lg py-12 "
    "border border-[#00D1B3]"   # ← era "border-1 border-[#00D1B3]"
)
CONTACTO_CARD_ROW_BOX = "w-full h-auto flex flex-col items-start justify-center"
CONTACTO_HEADER_TITULO_PRINCIPAL = "text-davs-color-morado-claro text-3xl font-bold "
CONTACTO_BODY_FOTO_BASE = (
    "h-[200px] w-[200px] "
    "rounded-full "               
    "border-2 border-davs-color-cian "
    "bg-davs-color-base "               
    "overflow-hidden "            
    "flex justify-center items-center"
)
CONTACTO_BODY_FOTO = (
    "w-full h-full object-cover "
    "scale-[1.3]"                 
)
CONTACTO_BOTON_ANIMACION_BASE = (
    "h-[60px] w-[60px] rounded-full " 
    "flex justify-center items-center " 
    "bg-davs-color-base "               
)
CONTACTO_LOGO_IMG = "h-full w-full object-contain p-[14px] "
CONTACTO_LOGO_ICON = "text-davs-color-cian"
CONTACTO_TEXTO_LINK = "text-davs-color-morado-claro text-lg font-medium hover:text-white transition-colors cursor-pointer"


# ==========================================
# FOOTER STYLES
# ==========================================
FOOTER_BASE = (
    "w-full h-[70px] bg-davs-color-base "
    "flex justify-between items-center px-10 " 
    "border-t border-[#1A2332]"
)
FOOTER_TEXT = "text-sm font-medium text-davs-color-morado-oscuro"
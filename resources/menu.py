from colors import TextColors

# Objeto para establecer colores al texto
text = TextColors

# Impresión de todo el menú del programa
class Menu:
    
    def __init__(self) -> None:
        self.main_menu = f"{text.yellow}Tablas para segmentos de red IPv4{text.reset}"
        self.options = {
            1: f"{text.cyan}Segmentos en consola{text.reset}",
            2: f"{text.cyan}Segmentos en Excel{text.reset}",
            3: f"{text.cyan}Segmentos en consola y Excel{text.reset}",
            4: f"{text.cyan}Salir{text.reset}"
        }
        self.select = f"{text.yellow}Opción: {text.reset}"

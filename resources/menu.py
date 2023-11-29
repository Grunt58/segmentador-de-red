from resources import colors

# Objeto para establecer colores al texto
text = colors.TextColors

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

    def show_menu(self) -> str:
        return self.main_menu
    
    # Imprime la lista de opciones y toma la elección del usuario
    def get_user_input(self) -> int:
        for index, value in self.options.items():
            print(f"{index}: {value}")

        try:
            user_input = int(input(self.select))
            return user_input
        except ValueError as err:
            print(f"{text.red}[{err}]: Solo números enteros.{text.reset}")
            return 0
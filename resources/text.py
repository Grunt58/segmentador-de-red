from resources import colors
import os, platform

# Objeto para establecer colores al texto
color: object = colors.TextColors

# Impresión de todo el menú del programa
class Menu:
    
    def __init__(self) -> None:
        self.main_menu: str = f"{color.yellow}Tablas para segmentos de red IPv4{color.reset}"
        self.options: dict = {
            0: f"{color.cyan}Salir{color.reset}",
            1: f"{color.cyan}Segmentos en consola{color.reset}",
            2: f"{color.cyan}Segmentos en Excel{color.reset}",
            3: f"{color.cyan}Segmentos en consola y Excel{color.reset}",
            4: f"{color.cyan}Multiples redes a Excel{color.reset}"
        }
        self.select = f"{color.yellow}Opción: {color.reset}"

    def show_menu(self) -> str:
        return self.main_menu
    
    # Imprime la lista de opciones y toma la elección del usuario
    def get_user_input(self) -> int:
        for index, value in self.options.items():
            print(f"{index}: {value}")

        try:
            user_input: int = int(input(self.select))
            return user_input
        except ValueError as err:
            print(f"{color.red}[{err}]: Solo números enteros.{color.reset}")
            return 0

'''
FONT INFORMATION (ASCII ART)

"Big" by Glenn Chappell 4/93 -- based on Standard
Includes ISO Latin-1
Greek characters by Bruce Jakeway <pbjakeway@neumann.uwaterloo.ca>
figlet release 2.2 -- November 1996
Permission is hereby given to modify this font, as long as the
modifier's name is placed on a comment line.

Modified by Paul Burton <solution@earthlink.net> 12/96 to include new parameter
supported by FIGlet and FIGWin. May also be slightly modified for better use
of new full-width/kern/smush alternatives, but default output is NOT changed.
'''
ASCII_ART = """ ________________________________________________________________________________________________
|   _____                                 _            _              _____ _____        _  _    |
|  / ____|                               | |          | |            |_   _|  __ \\      | || |   |
| | (___   ___  __ _ _ __ ___   ___ _ __ | |_ __ _  __| | ___  _ __    | | | |__) |_   _| || |_  |
|  \\___ \\ / _ \\/ _` | '_ ` _ \\ / _ \\ '_ \\| __/ _` |/ _` |/ _ \\| '__|   | | |  ___/\\ \\ / /__   _| |
|  ____) |  __/ (_| | | | | | |  __/ | | | || (_| | (_| | (_) | |     _| |_| |     \\ V /   | |   |
| |_____/ \\___|\\__, |_| |_| |_|\\___|_| |_|\\__\\__,_|\\__,_|\\___/|_|    |_____|_|      \\_/    |_|   |
|               __/ |                                                                            |
|              |___/                                                                             |
|________________________________________________________________________________________________|
"""

ABOUT = f""" ________________________________________________________________________________________________
|                                                                                                |
|                       {color.bright_red}This is v3.2.0 of "Segmentador de redes IPv4"{color.reset}                            |
|           Visit: {color.bright_blue}{color.underline}https://github.com/Grunt58/segmentador-de-red/releases{color.reset} for updates.           |
|________________________________________________________________________________________________|
"""

RUNNIGN_ON = f"""Python version: {color.bright_green}{platform.python_version()}{color.reset}
Python compiler: {color.bright_green}{platform.python_compiler()}{color.reset}
Running on: {color.bright_green}{platform.system()} {platform.release()} ({os.name}) ({platform.version()}){color.reset}
"""
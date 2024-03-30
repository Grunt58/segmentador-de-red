'''
Colores que serán utilizados para 'colorear' los mensajes en consola

Add Text Color to Python Terminal Programs:
    https://www.youtube.com/watch?v=CiNMlZxwet0

For more colors, check:
    https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
'''
class TextColors:
    # Base text colors
    black = "\u001b[30m"
    red = "\u001b[0;31m"
    green = "\u001b[0;32m"
    yellow = "\u001b[0;33m"
    blue = "\u001b[0;34m"
    magenta = "\u001b[0;35m"
    cyan = "\u001b[0;36m"
    white = "\u001b[0;37m"
    # Bright version text colors
    bright_black = "\u001b[30;1m"
    bright_red = "\u001b[31;1m"
    bright_green = "\u001b[32;1m"
    bright_yellow = "\u001b[33;1m"
    bright_blue = "\u001b[34;1m"
    bright_magenta = "\u001b[35;1m"
    bright_cyan = "\u001b[36;1m"
    bright_white = "\u001b[37;1m"

    # Background colors
    background_black = "\u001b[40m"
    background_red = "\u001b[41m"
    background_green = "\u001b[42m"
    background_yellow = "\u001b[43m"
    background_blue = "\u001b[44m"
    background_magenta = "\u001b[45m"
    background_cyan = "\u001b[46m"
    background_white = "\u001b[47m"
    # Bright version background colors
    background__bright_black = "\u001b[40;1m"
    background_bright_red = "\u001b[41;1m"
    background_bright_green = "\u001b[42;1m"
    background_bright_yellow = "\u001b[43;1m"
    background_bright_blue = "\u001b[44;1m"
    background_bright_magenta = "\u001b[45;1m"
    background_bright_cyan = "\u001b[46;1m"
    background_bright_white = "\u001b[47;1m"

    # Text formating
    underline = "\u001b[4m"
    bold = "\u001b[1m"
    inverse = "\u001b[7m"
    reset = "\u001b[0m"
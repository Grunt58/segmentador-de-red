'''
Colores que serán utilizados para 'colorear' los mensajes en consola

Add Text Color to Python Terminal Programs:
    https://www.youtube.com/watch?v=CiNMlZxwet0

For more colors, check:
    https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
'''
class TextColors:
    red = "\u001b[0;31m"
    green = "\u001b[0;32m"
    yellow = "\u001b[0;33m"
    blue = "\u001b[0;34m"
    magenta = "\u001b[0;35m"
    cyan = "\u001b[0;36m"
    white = "\u001b[0;37m"
    underline = "\u001b[4m"
    bold = "\u001b[1m"
    inverse = "\u001b[7m"
    reset = "\u001b[0m"
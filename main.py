import os

from scripts import excel_tables
from scripts import network_segmentation
from resources import menu
from resources import colors

# Clase menú
main_menu: object = menu.Menu()
# Para colorear la consola
text: object = colors.TextColors

while True:
    main_menu.show_menu()
    user_input: int = main_menu.get_user_input()

    match user_input:
        case 1:
            network: str = str(input(f"{text.magenta}Dirección base: {text.reset}"))
            hosts: list = [int(host) for host in input(f"{text.magenta}Cantidad de hosts (separados por comas): {text.reset}").split(",")]

            new_segment: object = network_segmentation.Segments(network, hosts)

            for host in hosts:
                mask: int = new_segment.set_mask(host)
                new_segment.host_bits(mask)

                new_segment.next_segment(mask)

                new_segment.add_segment()
                curret_segment = f"SEGMENTO: {new_segment.get_total_segments()}"
                print(f"{text.green}{curret_segment:-^40}{text.reset}")
                new_segment.get_network_info()

        case 2:
            pass

        case 3:
            pass

        case 4:
            break

        case _:
            pass
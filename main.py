import os

from scripts import excel_tables
from scripts import network_segmentation
from resources import menu
from resources import colors

def clear() -> None:
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

# Clase menú
main_menu: object = menu.Menu()
# Para colorear la consola
text: object = colors.TextColors

while True:
    clear()
    main_menu.show_menu()
    user_input: int = main_menu.get_user_input()

    match user_input:
        case 1:
            network: str = str(input(f"{text.magenta}Dirección base: {text.reset}"))
            hosts: list[int] = [int(host) for host in input(f"{text.magenta}Cantidad de hosts (separados por comas): {text.reset}").split(",")]

            new_segment: object = network_segmentation.Segments(network, hosts)

            for host in hosts:
                mask: int = new_segment.set_mask(host)
                new_segment.host_bits(mask)

                new_segment.next_segment(mask)

                new_segment.add_segment()
                curret_segment = f"SEGMENTO: {new_segment.get_total_segments()}"
                print(f"{text.green}{curret_segment:-^40}{text.reset}")
                new_segment.get_network_info()

            input(f"\n\n\n{text.blue}Presiona enter para continuar...{text.reset}")

        case 2:
            network: str = str(input(f"{text.magenta}Dirección base: {text.reset}"))
            hosts: list[int] = [int(host) for host in input(f"{text.magenta}Cantidad de hosts (separados por comas): {text.reset}").split(",")]
            file_name: str = str(input(f"{text.magenta}Nombre de archivo: {text.reset}"))

            new_segment: object = network_segmentation.Segments(network, hosts)
            table: object = excel_tables.Red_Segmentada(network, file_name)
            table.create_file()

            for host in hosts:
                new_segment.add_segment()

                mask: int = new_segment.set_mask(host)
                new_segment.host_bits(mask)

                new_segment.next_segment(mask)

                segment_to_table: list[str] = new_segment.export_network_info()
                segment_to_table.insert(0, new_segment.get_total_segments())
                table.add_segment(segment_to_table)

            table.create_table(new_segment.get_total_segments())
            print(f"{text.green}Los datos fueron exportados exitosamente.{text.reset}")

            input(f"\n\n\n{text.blue}Presiona enter para continuar...{text.reset}")

        case 3:
            network: str = str(input(f"{text.magenta}Dirección base: {text.reset}"))
            hosts: list[int] = [int(host) for host in input(f"{text.magenta}Cantidad de hosts (separados por comas): {text.reset}").split(",")]
            file_name: str = str(input(f"{text.magenta}Nombre de archivo: {text.reset}"))

            new_segment: object = network_segmentation.Segments(network, hosts)
            table: object = excel_tables.Red_Segmentada(network, file_name)
            table.create_file()

            for host in hosts:
                new_segment.add_segment()

                mask: int = new_segment.set_mask(host)
                new_segment.host_bits(mask)

                new_segment.next_segment(mask)

                curret_segment = f"SEGMENTO: {new_segment.get_total_segments()}"
                print(f"{text.green}{curret_segment:-^40}{text.reset}")
                new_segment.get_network_info()

                segment_to_table: list[str] = new_segment.export_network_info()
                segment_to_table.insert(0, new_segment.get_total_segments())
                table.add_segment(segment_to_table)

            table.create_table(new_segment.get_total_segments())
            print(f"{text.green}Los datos fueron exportados exitosamente.{text.reset}")

            input(f"\n\n\n{text.blue}Presiona enter para continuar...{text.reset}")

        case 4:
            break

        case _:
            print(f"{text.red}[ERROR]: La opción es entre 1 a 4.{text.reset}")

            input(f"\n\n\n{text.blue}Presiona enter para continuar...{text.reset}")
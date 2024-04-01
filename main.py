import os

from scripts import excel_tables
from scripts import network_segmentation
from resources import text
from resources import colors

# Clase menú
main_menu: object = text.Menu()
# Para colorear la consola
color: object = colors.TextColors
# Separador
bar: str = "-"

# Limpia la consola
def clear() -> None:
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

# Ordena los hosts de mayor a menor
def ordered_hosts() -> list[int]:
    hosts: list[int] = [int(host) for host in input(f"{color.bright_magenta}Cantidad de hosts (separados por comas):{color.reset} ").split(",")]
    hosts.sort(reverse=True)
    return hosts

clear()
# Inicio del programa
print(text.ASCII_ART)
print(text.ABOUT)
print(text.RUNNIGN_ON)
input(f"{color.background_blue}Presiona {color.underline}Enter{color.reset}{color.background_blue} para continuar...{color.reset}")

while True:
    clear()
    main_menu.show_menu()
    user_input: int = main_menu.get_user_input()

    match user_input:
        case 0:
            break

        case 1:
            clear()
            print(text.SEG_TO_CONSOLE)
            # La dirección la cual será segmentada
            network: str = str(input(f"{color.bright_magenta}Dirección base:{color.reset} "))
            print(f"{color.magenta}{bar*15}{color.reset}")
            # Cantidad de host por segmento
            hosts: list[int] = ordered_hosts()
            print("\n")

            new_segment: object = network_segmentation.Segments(network, hosts)

            # Calcular y mostrar información para cada subred
            for host in hosts:
                # Establece la máscara de la subred
                mask: int = new_segment.set_mask(host)
                new_segment.host_bits(mask)

                # Información general de la subred
                new_segment.next_segment(mask)

                # Segmento en el que estamos actualmente
                new_segment.add_segment()
                curret_segment: str = f"SEGMENTO: {new_segment.get_total_segments()}"
                print(f"{color.green}{curret_segment:-^40}{color.reset}")

                # Imprime la información de la subred
                new_segment.get_network_info()

            input(f"\n\n\n{color.background_blue}Presiona {color.underline}Enter{color.reset}{color.background_blue} para continuar...{color.reset}")

        case 2:
            clear()
            print(text.SEG_TO_EXCEL)
            network: str = str(input(f"{color.bright_magenta}Dirección base:{color.reset} "))
            print(f"{color.magenta}{bar*15}{color.reset}")
            hosts: list[int] = ordered_hosts()
            print(f"{color.magenta}{bar*15}{color.reset}")
            # Nombre para el archivo de Excel
            file_name: str = str(input(f"{color.bright_magenta}Nombre de archivo:{color.reset} "))
            print(f"{color.magenta}{bar*15}{color.reset}")

            new_segment: object = network_segmentation.Segments(network, hosts)
            table: object = excel_tables.Red_Segmentada(file_name)
            table.create_file()
            table.set_base_IP(network)

            for host in hosts:
                new_segment.add_segment()

                mask: int = new_segment.set_mask(host)
                new_segment.host_bits(mask)

                new_segment.next_segment(mask)

                # Exporta los datos de toda la rad segmentada a Excel
                segment_to_table: list[str] = new_segment.export_network_info()
                segment_to_table.insert(0, new_segment.get_total_segments())
                table.add_segment(segment_to_table)

            table.create_table(new_segment.get_total_segments(), network)
            table.close_file()
            print(f"{color.bright_green}Los datos fueron exportados exitosamente.{color.reset}")

            input(f"\n\n\n{color.background_blue}Presiona {color.underline}Enter{color.reset}{color.background_blue} para continuar...{color.reset}")

        case 3:
            clear()
            print(text.SEG_TO_CONSOLE_EXCEL)
            network: str = str(input(f"{color.bright_magenta}Dirección base:{color.reset} "))
            print(f"{color.magenta}{bar*15}{color.reset}")
            hosts: list[int] = ordered_hosts()
            print(f"{color.magenta}{bar*15}{color.reset}")
            file_name: str = str(input(f"{color.bright_magenta}Nombre de archivo:{color.reset} "))

            new_segment: object = network_segmentation.Segments(network, hosts)
            table: object = excel_tables.Red_Segmentada(file_name)
            table.create_file()
            table.set_base_IP(network)

            for host in hosts:
                new_segment.add_segment()

                mask: int = new_segment.set_mask(host)
                new_segment.host_bits(mask)

                new_segment.next_segment(mask)

                curret_segment: str = f"SEGMENTO: {new_segment.get_total_segments()}"
                print(f"{color.green}{curret_segment:-^40}{color.reset}")
                new_segment.get_network_info()

                segment_to_table: list[str] = new_segment.export_network_info()
                segment_to_table.insert(0, new_segment.get_total_segments())
                table.add_segment(segment_to_table)

            table.create_table(new_segment.get_total_segments(), network)
            table.close_file()
            print(f"{color.bright_green}Los datos fueron exportados exitosamente.{color.reset}")

            input(f"\n\n\n{color.background_blue}Presiona {color.underline}Enter{color.reset}{color.background_blue} para continuar...{color.reset}")

        case 4:
            clear()
            print(text.MULTIPLE_NETWORKS)
            file_name: str = str(input(f"{color.bright_magenta}Nombre de archivo:{color.reset} "))
            print(f"{color.magenta}{bar*15}{color.reset}")
            networks: str = [str(network) for network in input(f"{color.bright_magenta}Redes (separadas por comas):{color.reset} ").split(",")]
            print(f"{color.magenta}{bar*15}{color.reset}")
            table: object = excel_tables.Red_Segmentada(file_name)
            table.create_file()

            for network in networks:
                clear()
                print(text.MULTIPLE_NETWORKS)
                print(f"{color.bright_cyan}Red: {network}{color.reset}")
                print(f"{color.cyan}{bar*15}{color.reset}")
                table.set_base_IP(network)
                hosts: list[int] = ordered_hosts()
                new_segment: object = network_segmentation.Segments(network, hosts)

                for host in hosts:
                    new_segment.add_segment()

                    mask: int = new_segment.set_mask(host)
                    new_segment.host_bits(mask)

                    new_segment.next_segment(mask)

                    segment_to_table: list[str] = new_segment.export_network_info()
                    segment_to_table.insert(0, new_segment.get_total_segments())
                    table.add_segment(segment_to_table)

                table.create_table(new_segment.get_total_segments(), network)
                print(f"{color.bright_green}Los datos fueron exportados exitosamente.{color.reset}")

                input(f"\n\n\n{color.background_blue}Presiona {color.underline}Enter{color.reset}{color.background_blue} para continuar...{color.reset}")

            table.close_file()

        case _:
            print(f"{color.background_red}[ERROR]:{color.reset} {color.red}La opción es entre 0 a 4.{color.reset}")

            input(f"\n\n\n{color.background_blue}Presiona {color.underline}Enter{color.reset}{color.background_blue} para continuar...{color.reset}")
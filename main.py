import os

from scripts import excel_tables
from scripts import network_segmentation
from resources import text
from resources import colors

# Clase menú
main_menu: object = text.Menu()
# Para colorear la consola
color: object = colors.TextColors

# Limpia la consola
def clear() -> None:
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

# Ordena los hosts de mayor a menor
def ordered_hosts() -> list[int]:
    hosts: list[int] = [int(host) for host in input(f"{color.magenta}Cantidad de hosts (separados por comas): {color.reset}").split(",")]
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
            # La dirección la cual será segmentada
            network: str = str(input(f"{color.magenta}Dirección base: {color.reset}"))
            # Cantidad de host por segmento
            hosts: list[int] = ordered_hosts()

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

            input(f"\n\n\n{color.blue}Presiona enter para continuar...{color.reset}")

        case 2:
            network: str = str(input(f"{color.magenta}Dirección base: {color.reset}"))
            hosts: list[int] = ordered_hosts()
            # Nombre para el archivo de Excel
            file_name: str = str(input(f"{color.magenta}Nombre de archivo: {color.reset}"))

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
            print(f"{color.green}Los datos fueron exportados exitosamente.{color.reset}")

            input(f"\n\n\n{color.blue}Presiona enter para continuar...{color.reset}")

        case 3:
            network: str = str(input(f"{color.magenta}Dirección base: {color.reset}"))
            hosts: list[int] = ordered_hosts()
            file_name: str = str(input(f"{color.magenta}Nombre de archivo: {color.reset}"))

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
            print(f"{color.green}Los datos fueron exportados exitosamente.{color.reset}")

            input(f"\n\n\n{color.blue}Presiona enter para continuar...{color.reset}")

        case 4:
            file_name: str = str(input(f"{color.magenta}Nombre de archivo: {color.reset}"))
            networks: str = [str(network) for network in input(f"{color.magenta}Redes a las que segmentarás (separadas por comas): {color.reset}").split(",")]
            table: object = excel_tables.Red_Segmentada(file_name)
            table.create_file()

            for network in networks:
                print(f"Red: {network}")
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
                print(f"{color.green}Los datos fueron exportados exitosamente.{color.reset}")

            table.close_file()

        case _:
            print(f"{color.red}[ERROR]: La opción es entre 0 a 4.{color.reset}")

            input(f"\n\n\n{color.blue}Presiona enter para continuar...{color.reset}")
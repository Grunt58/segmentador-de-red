import ipaddress
from classes import excel_tables
from classes import network_segmentation

# Dirección base de la red
RAW_direccion_base = str(input("Dirección base: "))

# Solicitar al usuario la cantidad de hosts para cada red
host_solicitados = [int(x) for x in input("Introduce la cantidad de hosts para cada red (separados por comas): ").split(",")]
host_solicitados.sort(reverse=True)

segmentos = network_segmentation.Segments(RAW_direccion_base, host_solicitados)

archivo = str(input("Nombre del archivo: "))
tabla = excel_tables.Red_Segmentada(RAW_direccion_base, archivo)
tabla.create_file()


for num_hosts in host_solicitados:
    network_segmentation.Segments.add_segment()
    # Calcular la máscara de subred necesaria
    mascara = segmentos.set_mask(num_hosts)

    # Guarda la cantidad de bits activos por segmento
    segmentos.host_bits(mascara)

    # Genera la información del segmento actual
    segmentos.next_segment(mascara)

    # Muestra la información del segmento actual
    curret_segment = f"SEGMENTO: {network_segmentation.Segments.get_total_segments()}"
    print(f"{curret_segment:-^40}")
    segmentos.get_network_info()    

    # Exporta la información a Excel

    new_segment = segmentos.export_network_info()
    new_segment.insert(0, network_segmentation.Segments.get_total_segments())
    tabla.add_segment(new_segment)

# El parámetro sirve para saber la longitud de la tabla
tabla.create_table(network_segmentation.Segments.get_total_segments())
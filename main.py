import ipaddress
from classes import excel_tables

# Dirección base de la red
RAW_direccion_base = str(input("Dirección base: "))
direccion_base = ipaddress.IPv4Address(RAW_direccion_base)

# Solicitar al usuario la cantidad de hosts para cada red
host_solicitados = [int(x) for x in input("Introduce la cantidad de hosts para cada red (separados por comas): ").split(",")]
host_solicitados.sort(reverse=True)

archivo = str(input("Nombre del archivo: "))
tabla = excel_tables.Red_Segmentada(RAW_direccion_base, archivo)
tabla.create_file()

# Calcular y mostrar información para cada red
for index, num_hosts in enumerate(host_solicitados): # Se utilizó "enumerate" para saber en qué segmento estamos.
    # Calcular la máscara de subred necesaria
    bits_de_host = num_hosts.bit_length()
    mascara = 32 - bits_de_host
    host_encontrados = 2**(32 - mascara) - 2

    # Asegura que los host solicitados no superen a los encontrados
    if host_encontrados < num_hosts:
        mascara -= 1
        host_encontrados = 2**(32 - mascara) - 2

    # Guarda la cantidad de bits activos por segmento
    bits_activos = 8 - (32 - mascara)
    bits = []
    for i in range(8):
        if bits_activos > 0:
            bits.append(1)
        else:
            bits.append(0)
        bits_activos -= 1

    # Calcular la dirección de red
    direccion_red = ipaddress.IPv4Network((direccion_base, mascara), strict=False)

    # Calcular la dirección de broadcast
    direccion_br = direccion_red.broadcast_address

    # Calcular la primera y última IP utilizable
    primera_ip_utilizable = direccion_red.network_address + 1
    ultima_ip_utilizable = direccion_br - 1

    segmento = f"SEGMENTO: {index+1}"
    mascara_digital = ''.join(map(str,bits)) + "=/" + str(mascara)
    # Imprimir la información
    print(f"""
{segmento:-^40}
{"Host solicitados":.<30}{num_hosts}
{"Host encontrados":.<30}{host_encontrados}
{"Dirección de red":.<30}{direccion_red}
{"Máscara digital":.<30}{mascara_digital}
{"Máscara decimal":.<30}{str(direccion_red.netmask)}
{"Primera IP utilizable":.<30}{primera_ip_utilizable}
{"Última IP utilizable":.<30}{ultima_ip_utilizable}
{"Dirección de BR":.<30}{direccion_br}
""")
    

    tabla.add_segment([str(index+1), str(num_hosts), str(host_encontrados), str(direccion_red), str(mascara_digital), str(direccion_red.netmask), str(primera_ip_utilizable), str(ultima_ip_utilizable), str(direccion_br)])
    
    # Actualizar la dirección base para la siguiente red
    direccion_base += 2**(32 - mascara)

tabla.create_table()
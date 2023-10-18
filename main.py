import ipaddress

# Solicitar al usuario la cantidad de hosts para cada red
host_solicitados = [int(x) for x in input("Introduce la cantidad de hosts para cada red (separados por comas): ").split(",")]

# Dirección base de la red
direccion_base = ipaddress.IPv4Address("200.1.4.0")

# Calcular y mostrar información para cada red
for num_hosts in host_solicitados:
    # Calcular la máscara de subred necesaria
    bits_de_host = num_hosts.bit_length()
    mascara = 32 - bits_de_host

    # Calcular la dirección de red
    direccion_red = ipaddress.IPv4Network((direccion_base, mascara), strict=False)

    # Calcular la dirección de broadcast
    direccion_br = direccion_red.broadcast_address

    # Calcular la primera y última IP utilizable
    primera_ip_utilizable = direccion_red.network_address + 1
    ultima_ip_utilizable = direccion_br - 1

    # Imprimir la información
    print("Host solicitados:", num_hosts)
    print("Host encontrados:", 2**(32 - mascara) - 2)  # Restamos 2 para excluir la dirección de red y la de broadcast
    print("Dirección de red:", direccion_red)
    print("Máscara digital:", "/" + str(mascara))
    print("Máscara decimal:", str(direccion_red.netmask))
    print("Primera IP utilizable:", primera_ip_utilizable)
    print("Última IP utilizable:", ultima_ip_utilizable)
    print("Dirección de BR:", direccion_br)
    print()
    
    # Actualizar la dirección base para la siguiente red
    direccion_base += 2**(32 - mascara)
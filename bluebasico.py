def calcular_partes(ipv4, mascara):
    # Convertir la dirección IPv4 y la máscara a enteros
    ip_entero = int(ipv4.replace('.', ''))
    mascara_entero = int(mascara.replace('.', ''))

    # Calcular la parte de red y la parte de host
    parte_red = ip_entero & mascara_entero
    parte_host = ip_entero & (~mascara_entero & 0xFFFFFFFF)

    # Convertir las partes de red y host a formato decimal
    parte_red_decimal = '.'.join([str((parte_red >> i) & 0xFF) for i in (24, 16, 8, 0)])
    parte_host_decimal = '.'.join([str((parte_host >> i) & 0xFF) for i in (24, 16, 8, 0)])

    return parte_red_decimal, parte_host_decimal


# Pedir al usuario que ingrese la dirección IPv4 y la máscara de red
ipv4 = input("Ingresa la dirección IPv4: ")
mascara = input("Ingresa la máscara de red: ")

# Calcular las partes de red y host
parte_red, parte_host = calcular_partes(ipv4, mascara)

# Mostrar los resultados
print("Parte de red: ", parte_red)
print("Parte de host: ", parte_host)

   
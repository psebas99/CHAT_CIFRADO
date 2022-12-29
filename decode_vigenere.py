def vigenere_decode(mensaje):
    codificado = ''
    clave = 'Ingenieria'
    clave1 = clave + 20000 * clave
    cantidad = mensaje.count('')
    cantidad1 = cantidad - 1
    faltante = cantidad1 - 10
    for i in range(faltante):
        clave = clave + clave1[i]

    for j in range(cantidad1):
        a = ord(mensaje[j]) - 31
        b = ord(clave[j]) - 31
        c = a - b
        if c < 0:
            d = (a - b + 94) % 94
            codificado = codificado + chr(int(d + 31))
        if c >= 0:
            d = (a - b) % 94
            codificado = codificado + chr(int(d + 31))

    return codificado

def vig_code(mensaje):
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
        c = (a + b) % 94
        codificado = codificado + chr(int(c + 31))

    #print(codificado)
    return codificado


def deco_hamming(mensaje):
    from operator import xor
    import numpy as np
    lista = []
    aux = int
    p1 = int
    p2 = int
    p3 = int
    p4 = int
    e1 = int
    e2 = int
    e3 = int
    e4 = int
    er = int
    b1 = int
    b2 = int
    b3 = int
    b4 = int
    b5 = int
    b6 = int
    b7 = int
    b8 = int
    b10 = int
    b11 = int
    decodificado = ''
    correlativo = int

    cantidad = mensaje.count('')
    cantidad1 = cantidad - 1
    caracteres = int(cantidad1 / 11)
    codificado = ''

    for i in range(caracteres):
        a = 11 * i
        b = 11 * i + 10
        for j in range(a, b + 1):
            codificado = codificado + mensaje[j]

        lista.append(codificado)
        codificado = ''

    for m in range(caracteres):
        palabra = lista[m]
        for n in range(0, 11):
            if n == 0:
                b1 = int(palabra[0])
            if n == 1:
                b2 = int(palabra[1])
            if n == 2:
                b3 = int(palabra[2])
            if n == 3:
                b4 = int(palabra[3])
            if n == 4:
                b5 = int(palabra[4])
            if n == 5:
                b6 = int(palabra[5])
            if n == 6:
                b7 = int(palabra[6])
            if n == 7:
                b8 = int(palabra[7])
            if n == 8:
                b9 = int(palabra[8])
            if n == 9:
                b10 = int(palabra[9])
            if n == 10:
                b11 = int(palabra[10])

        p1 = xor(b3, b5)
        p1 = xor(p1, b7)
        p1 = xor(p1, b9)
        p1 = xor(p1, b11)
        p2 = xor(b3, b6)
        p2 = xor(p2, b7)
        p2 = xor(p2, b10)
        p2 = xor(p2, b11)
        p3 = xor(b5, b6)
        p3 = xor(p3, b7)
        p4 = xor(b9, b10)
        p4 = xor(p4, b11)

        e1 = xor(p1, b1)
        e2 = xor(p2, b2)
        e3 = xor(p3, b4)
        e4 = xor(p4, b8)
        er = (8 * e4) + (4 * e3) + (2 * e2) + (1 * e1)

        if er == 3:
            if b3 == 1:
                b3 = 0
            else:
                b3 = 1

        if er == 5:
            if b5 == 1:
                b5 = 0
            else:
                b5 = 1

        if er == 6:
            if b6 == 1:
                b6 = 0
            else:
                b6 = 1

        if er == 7:
            if b7 == 1:
                b7 = 0
            else:
                b7 = 1

        if er == 9:
            if b9 == 1:
                b9 = 0
            else:
                b7 = 1

        if er == 10:
            if b10 == 1:
                b10 = 0
            else:
                b10 = 1

        if er == 11:
            if b11 == 1:
                b11 = 0
            else:
                b11 = 1

        correlativo = (64 * b3) + (32 * b5) + (16 * b6) + (8 * b7) + (4 * b9) + (2 * b10) + (1 * b11)

        decodificado = decodificado + chr(correlativo + 31)

    return decodificado























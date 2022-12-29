def hamming(palabra):
    indicador = '11111111111'
    import math
    from operator import xor
    codificado = ''
    residuo = int
    aux = int

    d7 = int
    d6 = int
    d5 = int
    d6 = int
    d4 = int
    d3 = int
    d2 = int
    d1 = int
    p1 = int
    p2 = int
    p3 = int
    p4 = int
    a1 = int
    a2 = int
    a3 = int
    a4 = int
    a5 = int
    a6 = int
    a7 = int
    a8 = int

    for i in palabra:
        aux = ord(i) - 31

        a8 = aux % 2
        residuo = math.trunc((aux - a8) / 2)
        a7 = math.trunc(residuo % 2)
        residuo = math.trunc((residuo - a7) / 2)
        a6 = math.trunc(residuo % 2)
        residuo = math.trunc((residuo - a6) / 2)
        a5 = math.trunc(residuo % 2)
        residuo = math.trunc((residuo - a5) / 2)
        a4 = math.trunc(residuo % 2)
        residuo = math.trunc((residuo - a4) / 2)
        a3 = math.trunc(residuo % 2)
        residuo = math.trunc((residuo - a3) / 2)
        a2 = math.trunc(residuo % 2)
        residuo = math.trunc((residuo - a2) / 2)
        a1 = residuo

        d1 = a2
        d2 = a3
        d3 = a4
        d4 = a5
        d5 = a6
        d6 = a7
        d7 = a8

        p1 = xor(d1, d2)
        p1 = xor(p1, d4)
        p1 = xor(p1, d5)
        p1 = xor(p1, d7)
        p2 = xor(d1, d3)
        p2 = xor(p2, d4)
        p2 = xor(p2, d6)
        p2 = xor(p2, d7)
        p3 = xor(d2, d3)
        p3 = xor(p3, d4)
        p4 = xor(d5, d6)
        p4 = xor(p4, d7)

        codificado = codificado + str(p1) + str(p2) + str(d1) + str(p3) + str(d2) + str(d3) + str(d4) + str(p4) + str(
            d5) + str(d6) + str(d7)

    codificado = codificado + indicador
    return codificado



def enviar(mensaje):
    import serial
    import time

    lista = []

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

    def sendarduino(pckgs):
        arduino = serial.Serial('COM17', 4800)
        time.sleep(0.5)
        for n in pckgs:
            write = "{}".format(n).encode("utf-8")
            arduino.write(write)

        arduino.close()

    sendarduino(lista)

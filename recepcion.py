def recibir():
    import serial
    import time
    decode = ''
    receptor = serial.Serial("COM20", 4800)
    time.sleep(2)
    logico = False
    i = 0
    contar = False
    n = 0
    mensaje = ''
    leyendo = True

    while leyendo:
        for i in range(i * 11, 11 + i * 11):

            try:
                datos = receptor.read()
                datos1 = datos.decode('utf-8')

                decode = decode + datos1

            except Exception:
                print("Hay un error")
        i += 1

        p = str(decode)
        # print(p)
        if p == "11111111111":
            break
        mensaje = mensaje + p
        # print(mensaje)

        decode = ''

    #print(mensaje)
    return mensaje








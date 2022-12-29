def cesar_code(mensaje):
    mensaje3=''
    for i in mensaje:
        mensaje1=ord(i)
        mensaje2=mensaje1+2
        mensaje3=mensaje3+chr(mensaje2)
    #print(mensaje3)
    return mensaje3




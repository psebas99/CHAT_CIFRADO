import numpy as np
def hill_code(palabra):
    L=np.matrix([[35,53,12],[12,21,5],[2,4,1]])
    codificado=''
    def relleno (mensaje):
        relleno=' '
        cantidad=mensaje.count('')
        cantidad1=cantidad-1
        cantidad2=cantidad1%3

        if cantidad2==1:
            mensaje=mensaje+relleno+relleno

        if cantidad2==2:
            mensaje=mensaje+relleno
        return mensaje

    palabra=relleno(palabra)
    cantidad=palabra.count('')
    cantidad1=cantidad-1
    columnas=int(cantidad1/3)

    A=np.ones([3,columnas])
    B=np.matrix(A)
    a=0
    for i in range(columnas):
        for j in range(3):
            B[j,i]=int(ord(palabra[a]))-31
            a=a+1

    C=L*B
    D=C%94

    for m in range(columnas):
        for n in range (3):
            codificado=codificado+chr(int(D[n,m])+31)
    #print(codificado)
    return codificado




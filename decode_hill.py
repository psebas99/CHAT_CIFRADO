def hill_decode(mensaje):
    import numpy as np
    codificado=''
    L=np.matrix([[35,53,12],[12,21,5],[2,4,1]])
    M=np.linalg.inv(L)
    N=M%94

    cantidad=mensaje.count('')
    cantidad1=cantidad-1
    columnas=int(cantidad1/3)

    A=np.ones([3,columnas])
    B=np.matrix(A)
    a=0
    for i in range(columnas):
        for j in range(3):
            B[j,i]=int(ord(mensaje[a]))-31
            a=a+1

    C=N*B
    D=C%94


    for m in range(columnas):
        for n in range (3):
            codificado=codificado+chr(int((round(D[n,m],0))+31))

    return codificado



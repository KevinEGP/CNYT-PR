import LibreriaNumerosComplejos as lib

def sumaMatriz(A,B):
    """
    Esta función recibe como parametros dos matrices representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna la suma matricial
    como una lista de listas, si las dimensiones son correctas, de lo contrario retornar un mensaje
    de alerta.
    """
    M = []
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        for i in range(len(A)):
            M.append([])        
            for j in range(len(A[0])):
                M[i].append(lib.suma(A[i][j], B[i][j]))
        return M

    else:
        return 'Dimensiones incorrectas'

def restaMatrices(A,B):
    """
    Esta función recibe como parametros dos matrices representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna la resta matricial
    como una lista de listas, si las dimensiones son correctas, de lo contrario retornar un mensaje
    de alerta.
    """
    return sumaMatriz(A,inversoAditivoMatriz(B))

def inversoAditivoMatriz(A):
    """
    Esta función recibe como parametro una matriz representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna el inverso aditivo
    de la matriz como una lista de listas.
    """
    return escalarMatriz(A,(-1,0))

def escalarMatriz(A,k):
    """
    Esta función recibe como parametros una matriz representada con una lista de listas y
    un escalar que es un número complejo en forma de tupla. Retorna el producto escalar
    como una lista de listas.
    """
    M = []
    for i in range(len(A)):
        M.append([])
        for j in range(len(A[0])):
            M[i].append(lib.producto(A[i][j],k))
    return M

def transpuestaMatriz(A):
    """
    Esta función recibe como parametro una matriz representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna la transpuesta
    de la matriz como una lista de listas.
    """
    M = []
    for i in range(len(A[0])):
        M.append([])
        for j in range(len(A)):
            M[i].append(A[j][i])
    return M

def conjugadaMatriz(A):
    """
    Esta función recibe como parametro una matriz representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna la conjugada
    de la matriz como una lista de listas.
    """
    M = []
    for i in range(len(A)):
        M.append([])
        for j in range(len(A[0])):
            M[i].append(lib.conjugado(A[i][j]))
    return M

def dagaMatriz(A):
    """
    Esta función recibe como parametro una matriz representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna la adjunta o daga
    de la matriz como una lista de listas.
    """
    return transpuestaMatriz(conjugadaMatriz(A))

def productoMatriz(A,B):
    """
    Esta función recibe como parametros dos matrices representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna el producto matricial
    como una lista de listas, si las dimensiones son correctas, de lo contrario retornar un mensaje
    de alerta.
    """
    M = []
    if len(A[0]) == len(B):
        for i in range(len(A)):
            M.append([])        
            for j in range(len(B[0])):
                M[i].append((0,0))
                for k in range(len(B)):
                    M[i][j] = lib.suma(M[i][j], lib.producto(A[i][k], B[k][j]))
                    
        return M
    else:
        return 'Dimensiones incorrectas'

def productoInternoVectores(A,B):
    """
    Esta función recibe como parametros dos matrices representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna el producto interno
    como una lista de listas, si las dimensiones son correctas, de lo contrario retornar
    un mensaje de alerta.
    """
    if len(A[0])==1 and len(B[0])==1:
        return productoMatriz(dagaMatriz(A),B)[0][0]
    else:
        return 'Dimensiones incorrectas'

def normaVector(A):
    """
    Esta función recibe como parametro una matriz representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna la norma del 
    vector como una lista de listas, si las dimensiones son correctas, de lo contrario
    retornar un mensaje de alerta.
    """
    if len(A[0])==1:
        return (productoInternoVectores(A,A))[0]**0.5
    else:
        return 'Dimensiones incorrectas'

def distanciaVectores(A,B):
    """
    Esta función recibe como parametros dos vectores representados con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna la distancia entre
    los vectores como una lista de listas, si las dimensiones son correctas, de lo contrario
    retornar un mensaje de alerta.
    """
    return normaVector(restaMatrices(A,B))

def esMatrizHermitiana(A):
    """
    Esta función recibe como parametro una matriz representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna true o false si
    la matriz es hermitiana o no, respectivamente.
    """
    return dagaMatriz(A) == A

def matrizIdentidad(n):
    """
    Esta función recibe como parametro un entero. Retorna la matriz identidad de tamaño nxn.
    """
    M = []
    for i in range(n):
        M.append([])
        for j in range(n):
            if i != j:
                M[i].append((0,0))
            else:
                M[i].append((1,0))
    return M

def esMatrizUnitaria(A):
    """
    Esta función recibe como parametro una matriz representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna true o false si
    la matriz es unitaria o no, respectivamente.
    """
    B = productoMatriz(A,dagaMatriz(A))

    for i in range(len(A)):
        for j in range(len(A[0])):
            B[i][j] = (round(B[i][j][0],0),B[i][j][1])

    return B == matrizIdentidad(len(A))

def productoTensorial(A,B):
    """
    Esta función recibe como parametros dos matrices representadas con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna el producto tensorial
    de las matrices como una lista de listas.
    """
    M = []
    filasA = len(A)
    columnasA = len(A[0])
    filasB = len(B)
    columnasB = len(B[0])

    for i in range(filasA*filasB):
        M.append([])
        for j in range(columnasA*columnasB):
            M[i].append(lib.producto(A[i//filasB][j//columnasB],B[i%filasB][j%columnasB]))

    return M

def moduloCuadradoMatriz(A):
    """
    Esta función recibe como parametro una matriz representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna la matriz
    donde sus entradas son el modulo al cuadrado de ese valor como una lista de listas.
    """
    M = []
    for i in range(len(A)):
        M.append([])
        for j in range(len(A[0])):
            M[i].append(lib.moduloCuadrado(A[i][j]))
    return M

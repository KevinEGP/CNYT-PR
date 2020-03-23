import matplotlib.pyplot as plt
import LibreriaMatricesComplejas as l
import math

def simulador(M,V,k):
    V_final = V[:]
    if k > 0:
        M_dinamica = potenciaMatriz(M,k)
        V_final = l.productoMatriz(M_dinamica,V)
    estado = []
    for i in range(len(V_final)):
        estado.append(V_final[i][0][0])
    index = list(range(len(estado)))
    plt.bar(index,estado)
    plt.show()

def simuladorCuantico(M,V,k):
    V_final = V[:]
    if k > 0:
        M_dinamica = potenciaMatriz(M,k)
        V_final = l.productoMatriz(M_dinamica,V)

    V_final = l.moduloCuadradoMatriz(V_final)
    estado = []
    for i in range(len(V_final)):
        estado.append(V_final[i][0])
    index = list(range(len(estado)))
    plt.bar(index,estado)
    plt.suptitle('Estado despues de ' + str(k) + ' clics', fontsize=16)
    plt.show()


def ensamblar(M,N):
    return l.productoTensorial(M,N)

    
def potenciaMatriz(M,n):
    answer = l.matrizIdentidad(len(M))
    for i in range(n):
        answer = l.productoMatriz(answer,M)
    return answer

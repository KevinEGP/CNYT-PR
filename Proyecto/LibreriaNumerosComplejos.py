import math

"""
Este documento incluye funciones que nos permiten trabajar con numeros complejos.
El número complejo a+ib lo representaremos mediante la tupla (a,b).
"""

def suma(c1,c2):
    """
    Esta función recibe como parametros dos números complejos en forma de tupla
    y retorna la suma de estos numeros igualmente como una tupla.
    """
    return (c1[0] + c2[0], c1[1] + c2[1])

def resta(c1,c2):
    """
    Esta función recibe como parametros dos números complejos en forma de tupla
    y retorna la resta de estos numeros igualmente como una tupla.
    """
    return (c1[0] - c2[0], c1[1] - c2[1])

def producto(c1,c2):
    """
    Esta función recibe como parametros dos números complejos en forma de tupla
    y retorna el producto de estos numeros igualmente como una tupla.
    """
    return ((c1[0]*c2[0]) - (c1[1]*c2[1]), (c1[0]*c2[1]) + (c1[1]*c2[0]))

def cociente(c1,c2):
    """
    Esta función recibe como parametros dos números complejos en forma de tupla
    y retorna el cociente de estos numeros igualmente como una tupla.
    """
    return (((c1[0]*c2[0]) + (c1[1]*c2[1]))/(c2[0]*c2[0] + c2[1]*c2[1]), 
            ((c1[1]*c2[0]) - (c1[0]*c2[1]))/((c2[0]*c2[0]) + (c2[1]*c2[1])))

def modulo(c1):
    """
    Esta función recibe como parametro un número complejo en forma de tupla
    y retorna el modulo de este numero igualmente como una tupla.
    """
    return (((c1[0]**2)+(c1[1]**2))**(0.5))

def moduloCuadrado(c1):
    """
    Esta función recibe como parametro un número complejo en forma de tupla
    y retorna el modulo de este numero igualmente como una tupla.
    """
    return ((abs(c1[0])**2)+(abs(c1[1])**2))

def conjugado(c1):
    """
    Esta función recibe como parametro un número complejo en forma de tupla
    y retorna el conjugado de este numero igualmente como una tupla.
    """
    return (c1[0],-1*c1[1])

def potencia(c1,n):
    """
    Esta función recibe como parametro un número complejo en forma de tupla
    y retorna este numero elevado a la n-esima potencia en forma de una tupla.
    """
    answer = (1,0)
    for i in range(n):
        answer = producto(answer,c1)
    return answer

def pol(c1):
    """
    Esta función recibe como parametro un número complejo en forma de tupla
    y retorna este numero en coordenadas polares como una tupla.
    """
    return (modulo(c1), math.atan(c1[1]/c1[0]))

def rec(c1):
    """
    Esta función recibe como parametro un número complejo en forma de tupla
    y retorna este numero en coordenadas rectangulares como una tupla.
    """
    return (c1[0]*math.cos(c1[1]), c1[0]*math.sin(c1[1]))

def printP(c1):
    """
    Esta función recibe como parametro un número complejo en forma de tupla
    e imprime este numero en coordenadas polares.
    """
    print("%se^(i%s)" %(c1[0],c1[1]))

def printR(c1):
    """
    Esta función recibe como parametro un número complejo en forma de tupla
    e imprime este numero en coordenadas rectangulares.
    """
    print("%s + %si" %(c1[0],c1[1]))

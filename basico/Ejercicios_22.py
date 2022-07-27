# EJERCICIO 1

"""
    Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
    Escribir una tercera función que reciba un diccionario con los precios
    y porcentajes de una cesta de la compra, y una de las funciones anteriores, 
    y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.
    Ejemplo de diccionario: {1000:20, 500:10, 100:1}
"""
def apply_discount(price, discount):
    # TODO: retorna precio  menos precio con descuento dividido entre 100
    pass

def apply_IVA(price, percentage):
    # TODO: retorna el precio  suma precio por el porcentaje dividido por 100
    pass

def price_basket(basket, funcion):
    # TODO: retorna descuento o IVA
    pass

# EJERCICIO 2

"""
    Escribir una función que reciba otra función y una lista,
    y devuelva otra lista con el resultado de aplicar
    la función dada a cada uno de los elementos de la lista.
"""

def aplica_funcion_lista(funcion, lista):
    # TODO: recorrer la lista
    # TODO: apendizar los resultados de la función en una lista vacia
    # TODO: retorne la lista final
    pass

def cuadrado(n):
    # TODO: retorne n * n
    pass

# EJERCICIO 3

"""
    Escribir una función que reciba una frase y
    devuelva un diccionario con las palabras que contiene y su longitud.
    Ejemplo: "Hola Mundo" --> {"Hola": 4, "Mundo": 5}
"""
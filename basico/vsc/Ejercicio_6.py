# EJERCICIO 1

# Mínimo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40

# 1) Escribe el listado e ímprimelo
listado = [30, 20, 10, 50, 40]

# Descomentar para ejecutar:
# print(listado)

# 2) Prueba con min(listado)

def minimo(lista):
    return min(lista)

# Descomentar para ejecutar:
# print(minimo(listado))

# 3) Realiza lo mismo pero con bucles y condicionales

# una opción...

def minimo_2(lista):
    minimo = max(lista) + 1

    for numero in lista:
        if numero < minimo:
            minimo = numero

    return minimo

# Descomentar para ejecutar:
# print(minimo_2(listado))

# otra opción...

def minimo_3(lista):
    minimo = 1000000

    for numero in listado:
        if numero < minimo:
            minimo = numero

    return minimo

# Descomentar para ejecutar:
# print(minimo_3(listado))


# EJERCICIO 2

# Máximo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40

# 1) Escribe el listado e ímprimelo

print(listado)

# 2) Prueba con max(listado)

def maximo(lista):
    return max(lista)

# Descomentar para ejecutar:
# print(maximo(listado))

# 3) Realiza lo mismo pero con bucles y condicionales

# una opción...

def maximo_1(lista):
    maximo = -100000000

    for numero in listado:
        if numero > maximo:
            maximo = numero
    return maximo

# Descomentar para ejecutar:
# print(maximo_1(listado))

# otra opción...

def maximo_2(lista):
    maximo = -min(listado)-1

    for numero in listado:
        if numero > maximo:
            maximo = numero
    return maximo


# print(maximo_2(listado))


# EJERCICIO 3

# Ordena de menor a mayor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")

# Pista: si quieres almacena esos números en una lista de nombre: "listado_ascendente"

# 1) Escribe el listado e ímprimelo

# 2) Prueba a usar sort()

# 3) Realiza lo mismo pero con bucles y condicionales



# EJERCICIO 4

# Ordena de mayor a menor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")

# 1) Escribe el listado e ímprimelo

# 2) Prueba a usar sort()

# 3) Realiza lo mismo pero con bucles y condicionales


# EJERCICIO 5
"""
    Escribe el código necesario en Python para:

    * almacenar con una lista de nombre "módulos" las siguientes materias de un programa de Ciencia de Datos:

    * Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP.

"""
# 1) Para ese listado imprime todas ellas, 1 a 1

"""
    2) dentro de ese grupo de materias, existen unas materias que son básicas en todos los programas.

    y que forman la base de conocimientos iniciales para afrontar con éxito el resto de un programa.

    Las mismas son: Python y Algoritmos (aunque en la práctica hay más cosas)

    Se pide almacenar las mismas en un listado secundario, de nombre: "esenciales" (por ejemplo)

    Imprime ese listado al terminar de almacenarlos.
"""

"""
    3) Crea un DataFrame, de nombre df con esa información en base
    a la siguiente relación de módulos y horas de clase módulos:
    Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP

    horas: 25, 15, 5, 15, 5, 10
"""

# 4) De ese DataFrame, selecciona solamente la columna "horas" e imprímela

# 5) Muestra el gráfico (plot) para la columna "horas"

# 6) De ese DataFrame, selecciona solamente aquellas materias que tienen 20 o más horas de dedicación

# 7) De ese DataFrame, selecciona solamente aquellas materias que tienen menos de 10 horas de dedicación

# 8) De ese DataFrame, selecciona solamente (si fuera posible)
    # aquellas materias que tienen mas de 26 horas de dedicación

# 9) Apendiza, (si puedes), una nueva columna llamada "docente" con el instructor encargado de la materia.

    # Y cuyos nombres serán: Enrique, Susana, Juan, Ana, Laura, Patricia



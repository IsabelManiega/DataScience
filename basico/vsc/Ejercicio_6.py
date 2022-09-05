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
    Pendiente
"""
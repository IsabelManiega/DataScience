import pandas as pd
import numpy as np

# EJERCICIO 1

"""
    1) Haz un programa que calcule los múltiplos de 3

    Para ello primero debe preguntarse al usuario cuántos múltiplos desea añadir.

    Nota: Puedes usar un bucle while si lo deseas

"""

# 2) Haz lo mismo con np.arange


# EJERCICIO 2

"""
    Dado el listado del apartado 2

    Dada esta lista de variable "listado" y "valores": 10, 10, 20, 20, 20, 30, 40

    Se pide:
"""

# 1) Crea un DataFrame con esa información e imprímelo


# 2) Usa value_counts() para determinar cuántas repeticiones hay de cada número en esa columna


# 3) Haz un ".shape" a esa información del value_counts()

    # NOTA: Escribe: .shape justo al final


# 4) A esa misma instrucción con value_counts() escribe al final ".values"

    # Y veras la información..

    # pasa esa información a lista si puedes

    # y guarda ese listado como "repeticiones"


# 5) A esa información de value_counts() añade al final ".index"

    # Y pasa posteriormente a lista esa información

    # y guarda ese listado con el nombre: "valores"


# 6) Crea un DataFrame con 2 columnas,

    # 1 para "valores"

    # 1 para "repeticiones"

    # llámalo: "df_value_counts" (por ejemplo)

    # Y observa..


# 7) Haz lo siguiente: "df.value_counts()"

# 8) Observa si hay diferencias entre: "df" y "df_value_counts"



# EJERCICIO 3
"""
    Comparación de matrices

    Haz el código que testee si esas 2 matrices son iguales

    1)

    Dadas:

    matriz1 = np.array([[1,2],[3,4]])

    matriz2 = np.array([[1,2],[3,8]])

    PISTAS:

    -1- RECORRER MATRIZ1 Y MATRIZ2 CON LA PARAMETRIZACIÓN de i y j
    COMPROBAR: ( matriz1 [ i ][ j ] == matriz2 [ i ][ j ] )

    -2- crear una variable contador (inicializada en 0)
    y, cuando detecte, un número de una matriz en una posición concreta,

    y sea diferente del número que tiene LA OTRA MATRIZ..entonces..

    -3- incremento 1 unidad en dicho contador:
    SI los números son DISTINTOS

    --> entonces, que se incremente en 1 unidad..

    de tal manera que si ese contador=0 (al final)--> son todos iguales --> matriz1 = matriz2

    y si es distinto de 0 -> es que POR LO MENOS 1 vez encontró un número diferente

    matriz1 != matriz2

    -4- puedes usar np.arange( ) si lo deseas para las filas y para las columnas

    -5- recuerda el ejercicio del cronómetro para tener una referencia
"""
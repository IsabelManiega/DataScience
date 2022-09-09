import pandas as pd

# EJERCICIO 1

"""
    Cada número es la suma de los 2 anteriores:

    0-1-1-2-3-5-8-13-21-34...

    Se pide programar esa secuencia con Python.

    Nota:

    Apendiza elementos hasta tener 10 primeros resultados.

    (los 10 números indicados desde 0 hasta 34)

    Si sabes, hazlo de varias formas diferentes
"""


# EJERCICIO 2

# Cada número es la suma de los 2 anteriores:

# 0-1-1-2-3-5-8-13-21-34...

# Se pide programar para los números de fibonacci mayores de 1000

# Primero muestra los valores de 0 hasta 1000000, crea una lista
# con ese listado crea una segunda lista con los mayores de 1000



# EJERCICIO 3

# Se pide crear un NUEVO dataframe para cada uno de los siguientes casos

# planteados y que están relacionados con el Titanic DataSet

# (antes debéis de cargar el archivo como df)

# 1) Leer el archivo train.csv del titanic dataset

df = pd.read_csv("./src/train.csv")

# Descomentar para ejecutar:
# print(df)

# 2) Crear un dataframe de nombre df_sobreviven refiriéndose a un dataframe en el que todos los pasajeros sobreviven

    # NOTA: si al principio no estás seguro del resultado, puedes usar value_counts() para comprobar tu resultado

# 3) Crear un dataframe de nombre df__no_sobreviven refiriéndose a un dataframe en el que NINGUNO de los pasajeros sobrevive

# 4) DataFrame de hombres que no sobrevivieron en el titanic

# 5) DataFrame de hombres que si sobrevivieron en el titanic

# 6) DataFrame de mujeres que no sobrevivieron en el titanic

# 7) DataFrame de mujeres que si sobrevivieron en el titanic
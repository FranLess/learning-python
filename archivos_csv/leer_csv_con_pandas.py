import pandas as pd
archivo_uri = 'archivos_csv\\datos.csv'


# usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv(archivo_uri)
df2 = pd.read_csv(archivo_uri)

# obteniendo los datos de la columna nombre
nombres = df['nombre']

# ordenando el dataframe por edad
df_orden_ascendente = df.sort_values('edad')  # devuelve un dataframe anonimo

# ordenandolo de forma descendente
df_orden_descendente = df.sort_values(
    'edad', ascending=False)  # devuelve un dataframe anonimo

# contatenando 2 dataframes
df_concatenado = pd.concat([df, df2])

# accediendo a las primeras 3 filas con head()
primeras_filas = df.head(3)

# accediento a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

# accediendo a la cantidad de filas y columnas con shape
filas, columnas = df.shape

# obteniendo data estadistica del dataframe:
df_info = df.describe()

# accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2, 'edad']

# accediendo a la edad de la fila 2 con iloc (i, de indice/index)
elemento_especifico_iloc = df.iloc[2, 2]

# accdiendo a todos los apellidos con loc
apellidos_loc = df.loc[:, 'apellido']

# accediento a todos los apellidos con iloc
apellidos_iloc = df.iloc[:, 1]

# accdiento a la fila 3 con loc
fila_3 = df.loc[2, :]

# accediento a la fila 3 con iloc
fila_3 = df.iloc[2, :]

# accediendo a filas con edad mayor que 30 con loc
mayor_que_30 = df.loc[df['edad'] > 30, :]

print(mayor_que_30)

import pandas as pd

df = pd.read_csv('archivos_problemas\\datos.csv')

# cambiar el tipo de dato de un columna a string
df['edad'] = df['edad'].astype(str)

# mostrar el tipo de dato del primer elemento de la columna edad
print(type(df['edad'][0]))

# reemplazando los datos 'dalto' por 'maestro'
df['apellido'].replace('dalto', 'maestro', inplace=True)

# eliminando las filas con datos faltantes
# axis=0 son filas, axis=1 son columnas
df = df.dropna(axis=0)

# eliminando filas repetidas
df = df.drop_duplicates()

# creando un CSV con el dataframe resultante (limpio)
df.to_csv('archivos_problemas\\datos_limpios.csv')

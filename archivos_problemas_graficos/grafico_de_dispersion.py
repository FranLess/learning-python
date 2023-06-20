import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# crear el la relacion que tiene el tiempo invertido con el dinero ganado

df = pd.read_csv('archivos_problemas_graficos\\dispersion.csv')

# creando el grafico
sns.scatterplot(x='tiempo', y='dinero', data=df)

# mostrando el grafico
plt.show()

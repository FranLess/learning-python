# ESTAS FUNCIONES TRATAN DE EXPLICAR LOS PARAMETROS POSICIONALES
# O LOS DATOS RELACIONALES
# ESTOS TIPOS DE PARAMETROS SON EXPLICADOS MAS A PROFUNDIDAD
# EN EL ARCHIVO functions.py

# creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre, apellido, adjetivo="Tonto"):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'


frase_resultante = frase("Lucas", "Dalto", "inteligente")
print(frase_resultante)

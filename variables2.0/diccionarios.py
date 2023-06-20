# creando diccionarios con dict()
diccionario = dict(nombre='francisco', apellido='martinez')

# las listas no pueden ser claves y usamos frozentset para meter conjuntos
diccionario = {frozenset(['francisco', 'rancio']): 'fasd'}

# creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(['nombre', 'apellido'])

# creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(['nombre', 'apellido'], 'no se')

print(diccionario.get('nombre'))

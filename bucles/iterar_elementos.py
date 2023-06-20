animales = ['gato', 'perro', 'loro', 'cocodrilo']
numeros = [12, 23, 34, 45]

# iterando la lista animales
for animal in animales:
    print(f'ahora la variable animal es igual a: {animal}')

# iterando la lista numero y multiplicado cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

# iteando dos listas del mismo tamaño al mismo tiempo
for numero, animal in zip(animales, numeros):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')

# forma correcta de recorrer una lista con su indice y valor
# parecido al foreach as key=>value de php
for key, value in enumerate(animales):
    print(f'el indice es: {key} y el valor es: {value}')

# usando el for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print('el bucle terminó')

# LO ANTERIOR FUNCIONA PARA TUPLAS Y CONJUNTOS, LOS DICCIONARIOS CAMBIAN UN POCO

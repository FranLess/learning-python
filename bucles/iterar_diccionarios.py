diccionario = {
    'nombre': 'francisco',
    'apellido': 'martinez',
    'subs': 1000000
}

# recorriendo diccionario para obtener las keys
for key in diccionario:
    print(f'la clave es: {key}')

# recorriendo diccionario con items() para obtener las claves y los valores
# las key=> se desempaquetan
for key, value in diccionario.items():
    print(f'la clave es: {key} y el valor es: {value}')

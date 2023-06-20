# creando las listas
frutas = ["banana", "manzana", "ciruela",
          "pera", "naranja", "granada", "durazno"]
cadena = "Hola Dalto"
numeros = [2, 5, 8, 10]

# evitando que se coma una manzana con la sentencia "continue"
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'me voy a comer una {fruta}')


print('-----------')
# evitar que el bucle siga ejecutandose
# (el else tampoco se ejecuta)
for fruta in frutas:
    print(f'me voy a comer una {fruta}')
    if fruta == 'pera':
        break
else:
    print('fin del bucle')

# recorrer una cadena de texto
for letra in cadena:
    print(letra)

# for en una sola linea de codigo
# (la logica de la variable a manipular va antes del for)

numeros_multiplicados_por_dos = [x*2 for x in numeros]
print('bucle en una sola linea')
print(numeros_multiplicados_por_dos)

# para poder hacer un bucle for en una linea hay que encerrarlo en []
otros_numeros = [print(x) for x in numeros]
print(otros_numeros)

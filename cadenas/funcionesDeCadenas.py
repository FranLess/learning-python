cadena1 = '''hola soy francisco'''
cadena2 = '''hola soy nib'''

# metodo para poner cadenas en mayusculas
mayuscula = cadena1.upper()
print(mayuscula)

# metodo para poner cadenas en minusculas
minuscula = cadena2.lower()
print(minuscula)

# metodo para capitalizar cadenas
capitalizada = cadena1.capitalize()
print(capitalizada)


buscar_cadena = 'hola'
# devuelve la posicicion de la cadena en la que empieza la cadena buscada

# buscar una cadena en otra cadena, devuelve -1 si no encuentra nada
cadena_find = cadena1.find(buscar_cadena)
print(cadena_find)

# busca una cadena en otra cadena, devuelve una excepcion si no encuentra nada
cadena_index = cadena2.index(buscar_cadena)
print(cadena_index)

# comprobar si es numerico
numero = '12312312311'
es_numerico = numero.isnumeric()
print(es_numerico)

# comprobar si el alfanumerico
alfanumerico = 'asdfas'
es_alfanumerico = alfanumerico.isalpha()
print(es_alfanumerico)

# contar coincidencias dentro de una cadena, si no encuentra devuelve 0
contrar_coincidencias = cadena1.count('hola')
print(contrar_coincidencias)

# contar los caracteres de una cadena
longitud = len(cadena1)
print(longitud)

# comprobar si un cadena empieza con otra cadena (true or false)
empieza_con = cadena1.startswith('hola')
print(empieza_con)

# comprobar si un cadena termina con otra cadena (true or false)
termina_con = cadena1.endswith('hola')
print(termina_con)

# reemplazar una cadena que se encuentre en la cadena con otra
cadena_con_comas = 'hola,como,estas,cola'
cadena_separada = cadena_con_comas.replace(',', ' ')
print(cadena_con_comas)
print(cadena_separada)

# separa la cadena con la cadena indicada y devuelve las separaciones en un lista
lista_split = cadena_con_comas.split(',')
print(lista_split)

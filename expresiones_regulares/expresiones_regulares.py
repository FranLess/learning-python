# EXPLICACION DE QUE HACE CADA COSA EN UNA EXPRESION REGULAR

import re  # libreria estandar de python para regex

texto = '''Hola maestro. esta es la cadena 1. Como estas mi capitan
Esta es la linea 2662598 de texto.
Esta es la linea 2 de texto.
Y Esta es la final (linea 3) definitiva mi capitan'''

# haciendo una busqueda simple, se puede pasar el parametro de flags
# para modificar el tipo de busqueda que se quiere realizar
# en este caso se indica que NO SEA SENSITIVE CASE
resultado = re.findall('Esta', texto, flags=re.IGNORECASE)

# \d -> busca digitos numericos del 0-9 [0-9]
resultado = re.findall(r'\d', texto)

# D -> busca digitos no numericos [a-z A-Z]
resultado = re.findall(r'\D', texto)

# \w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r'\w', texto)

# \W -> bucsca caracteres no alfanumericos
resultado = re.findall(r'\W', texto)

# \s -> busca espacios en blanco -> espacios, tabs, saltos de linea
resultado = re.findall(r'\s', texto)

# \S busca todo menos espacios en blanco
resultado = re.findall(r'\S', texto)

# . -> busca todo menos saltos en linea
resultado = re.findall(r'.', texto)

# \n -> busca saltos en linea
resultado = re.findall(r'\n', texto)

# \ -> cancela la funcion de caracteres especiales en regex
# como la funcion del '.' para buscar todo menos saltos de linea
# en este caso de buscaran puntos en lugar de algo que no sea \n
resultado = re.findall(r'\.', texto)

# ^ -> busca el comienzo de una linea (buscando hola al principio de la linea)
# flags=re.M activa la multilinea
resultado = re.findall(r'^Esta', texto, flags=re.M)

# $ -> busca el final de una linea
resultado = re.findall(r'capitan$', texto, flags=re.M)

# {n} -> repite n veces la busqueda que la antecede
# en este caso se busca 3 numeros juntos pues \d\d\d
resultado = re.findall(r'\d{3}', texto)

# {n,m} -> rango de minimo y maximo
# busca al menos dos numeros que esten juntos
# y maximo 4 que esten juento tambien
resultado = re.findall(r'\d{2,4}')

# | -> busca una cosa o la otra, como un 'or'
# busca 2 o 4 numeros pegados o tambien el texto 'Hola'
resultado = re.findall(r'\d{2,4}|Hola', texto)


# PARA CAER EN CUENTA DE LO QUE RESULTA EN CADA BUSQUEDA CON REGEX
# SERIA BUENO QUE IMPRIMAS EL RESULTADO UNA LINEA ABAJO DE LA BUSQUEDA
# Y ASI PUEDAS VER EL RESULTADO DE LA BUSQUEDA
print(resultado)

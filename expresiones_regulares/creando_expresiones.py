# creando una regex para buscar un numero
# en este caso para entender que un numero es mexicano
# y que es especificamente de durango

import re

# aqui entiendo que el '() ->' define el tipo de dato
# que la funcion returna


def numero_durango(numero: str) -> bool:
    pattern = r'\+52\s618\s\d{3}\s\d{4}'
    find = bool(re.search(pattern, numero))
    return find


numero_es_durango = numero_durango('+52 618 275 0981')

if numero_es_durango:
    print('el número es de durango')
else:
    print('el número no es de durango')

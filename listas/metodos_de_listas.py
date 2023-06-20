# crear un lista con list
lista = list()
print(lista)

# logitud de la lista, elementos que contiene la lista
lista_len = list(['hola', 'cola', 'pa ti', 123])
longitud_de_lista = len(lista_len)
print(longitud_de_lista)

# agregar elementos a una lista con append
lista.append('hola')
print(lista)

# agregar con insert
lista.insert(2, 'toma mama')
print(lista)

# agregando varios elementos a la lista
lista.extend(['toma mama', 123, True])
print(lista)

# eliminando un elemento de la lista
lista.pop(0)
print(lista)
# eliminar el ultimo elemento de la lista
lista.pop(-1)
print(lista)

# eliminar el elemento de la lista por su valor, si no hay elemento devuelve una excepcion
lista.remove('toma mama')
print(lista)

# ordenar una lista que contiene numeros o boleanos false primero, true despues
lista_de_numeros = [1, 2, 7, 22, 51, 345,
                    7356, 94, 7, True, False, False, False]
lista_de_numeros.sort()
print(lista_de_numeros)

# ordenar una lista de mayor a menor, con numero y boleanos
lista_de_numeros.reverse()
print(lista_de_numeros)

# encontrar elementos en una lista, tira un excepcion si no encuentra el elemento
index_de_elemento = lista_de_numeros.index(False)
print(index_de_elemento)

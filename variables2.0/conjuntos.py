# Creando un conjunto con set()
conjunto = set(['dato1'])

# metiendo un conjunto dentro de otro conjuto
conjunto1 = frozenset(['dato1', 'dato2'])
conjunto2 = {conjunto1, 'dato3'}

print(conjunto2)

# Teoria de conjuntos
conjunto1 = {1, 3, 5, 7}
conjunto2 = {2, 4, 7, 8}

# verificando si conjunto2 es un subconjunto del 1
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

# verificando si conjunto2 es un superconjunto del 1
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

# verificar si hay algún número en común
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)

# un diccionario es practicamente un objeto, no se como se llaman
# algo asi como una funcion anonima, funciona como un objeto, pero no pertenece a una clase en especial
# Rectificacion: los diccionarios se definen como si fueran un objeto
# pero no se puede acceder a sus elementos como si fueran objetos,
# se accede a sus elementos por medio de [] como si fura un array


diccionario = {"nombre": "Juan", "apellido": "Perez", "edad": 25}
# los dos siguientes elementos se iteran para acceder a los valores
# obtener los keys de el diccionario
claves = diccionario.keys()
print(claves)

# obtener los values de el diccionario
values = diccionario.values()
print(values)

# obtener el valor de un elemento
# acceder asi, tira una excepcion
# valor_de_hola = diccionario['hola']
valor_de_hola = diccionario.get("hola")
print(valor_de_hola)

# Eliminando un elemento de un diccionario
diccionario.pop("nombre")
print(diccionario)

# Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

# eliminando todo del diccionario
diccionario.clear()
print(diccionario)

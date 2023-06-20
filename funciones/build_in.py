# las funciones build in son funciones que vienen con el lenguaje
numeros = [4, 7, 1]

# encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)

# encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)

# redondeando a 3 decimales
numero = round(12.12315, 3)

# retornando el valor booleano que un dato devolveria
resultado_bool = bool('123')  # true
resultado_bool = bool(1)  # true
resultado_bool = bool(0)  # false
resultado_bool = bool([])  # false
resultado_bool = bool(None)  # false


# returnando si todos los valores son true o false si alguno no lo es
resultado_all = all([0, True, 123, 'asdf'])  # false
resultado_all = all([1, True, 123, 'asdf'])  # true

# suma todos los valores de un iterable
suma_total = sum(numeros)

print(suma_total)

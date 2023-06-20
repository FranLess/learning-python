# BASICAMENTE LO QUE SE EXPLICA AQUI SON LOS PARAMETROS EMPAQUETADOS
# ES DECIR LOS PARAMETROS QUE OBTIENEN UN CONJUNTO DE DATOS SEPARADOS
# EN UNA SOLA VARIABLE QUE SE PUEDE ITERAR

# MUY SIMILAR A ... EN JavaScript y PHP

# forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])


resultado2 = suma_total([5, 3, 9, 10, 20, 3])


# lo mismo que arriba pero utilizando el operador * como parametro (*args)
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"


resultado = suma("Lucas", 5, 3, 9, 10, 20, 3)

print(resultado)

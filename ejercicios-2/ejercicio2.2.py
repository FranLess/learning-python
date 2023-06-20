# creando una funciòn que nos devuelva los numeros primos
# entre 0 y el argumento que pasamos

# crear una funcion que verifique si un numero es primo
def es_primo(num):
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True


# creando funcion que retorne una lista con todos los primos
def primos_hasta(num):
    primos = []
    for i in range(3, num+1):
        resultado = es_primo(i)
        if resultado == True:
            primos.append(i)

    return primos


# creamos el resultado llamando a la funciòn y lo mostramos
resultado = primos_hasta(98)
print(resultado)

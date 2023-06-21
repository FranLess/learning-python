# creando funcion que suma numeros
def sumar_dos():
    # iniciando un bucle
    while True:
        # pidiendo numeros
        a = input('Numero 1: ')
        b = input('Numero 2: ')
        # intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b)
        # si lanzo una excepcion, pedirle que reingrese los datos
        # except es como el catch en PHP y JavaScript
        except Exception as e:
            print('Te pedi un numero salame, no te hagas el gracioso')
            print(f'ERROR: {e}')
        # else se ejecuta si no se lanza una excepcion
        else:
            break
        # finally se ejecuta siempre que el try se ejecuta
        finally:
            print('Esto se ejecuta siempre')

    return resultado


print(sumar_dos())

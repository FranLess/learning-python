# creando mi propia excepcion personalizada
# en python para heredar clases, se ponen dentro del parentesis de la clase
class MiExcepcion(Exception):
    def __init__(self, *args: object) -> None:
        if 'err' in args:
            index = args.index('err')
            value = args[index]
            # Utiliza el valor de 'err' para realizar alguna acción
            print("El valor de 'err' es:", value)


raise MiExcepcion('asdf')

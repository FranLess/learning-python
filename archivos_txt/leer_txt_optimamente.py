# abriendo el archivo con with open
with open('archivos_txt\\texto.txt') as archivo:
    # leemos el archivo
    contenido = archivo.read()

    # mostramos el archivo
    print(contenido)

# NO ES NECESARIO CERRAR EL ARCHIVO CON with open():

# usando open para abrir un archivo con una codificacion universal (UTF-8)
archivo = open("archivos_txt\\texto.txt", encoding='UTF-8')

# leer el archivo completo
# archivo = archivo.read()

# leer una sola linea
# linea = archivo.readline()

# leer linea por linea
lineas = archivo.readlines()

# cerrar el archivo
archivo.close()

print(lineas)

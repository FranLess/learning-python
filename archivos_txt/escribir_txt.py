# si escribimos un archivo y no encuentra el archivo se crea uno nuevo
with open('archivos_txt\\text.txt', 'a', encoding='UTF-8') as archivo:
    # sobreescribiendo el archivo
    archivo.write('jajjaja te la recontra teclee')

    # agregando 2 lineas con writelines
    archivo.writelines(['- hola maestro como andas\n', '- misericordia\n'])

    # agregando otras 2 lineas
    archivo.writelines(['hola pati mi cola\n', 'te recontra cagué\n'])

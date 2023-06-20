frase = input('dime y una frase y te calculo cuanto tardarias en decirla: \n')
palabras_separadas = frase.split(' ')
cantidad_de_palabras = len(palabras_separadas)

segundos_para_pronunciar = cantidad_de_palabras / 2
segundos_para_pronunciar_dalto = cantidad_de_palabras * 10 // (2 * 1.30)/10
print(f'Tú tardarías {segundos_para_pronunciar} segundos en decirlo')
print(f'Dalto tardaría {segundos_para_pronunciar_dalto} en decirlo')

if (cantidad_de_palabras >= 120):
    print('tampoco te pedi una biblia')

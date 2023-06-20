# promedio de duracion en hrs
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso_promedio = 1.5

# Duracion de videos en crudo
promedio_crudo = 5
dalto_crudo = 3.5

# diferencia de duracion entre el curso de dalto y otros
diferencia_min = 100 - dalto_curso_promedio / otros_cursos_min * 100
diferencia_max = 100 - dalto_curso_promedio * 1000 // otros_cursos_max / 10
diferencia_promedio = 100 - dalto_curso_promedio / otros_cursos_promedio * 100

# calcular el porcentaje de tiempo vacio promedio
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // promedio_crudo / 10
tiempo_vacio_dalto = 100 - dalto_curso_promedio * 1000 // dalto_crudo / 10

# Tiempo equivalente a ver 10 horas de curso de dalto y 10 horas de otros
diez_horas_dalto = otros_cursos_promedio * 100 // dalto_curso_promedio / 10
diez_horas_promedio = dalto_curso_promedio / otros_cursos_promedio * 10

print('----------------------------------------')

# Tiempos promedio de duracion
print(f'El curso de dalto dura un {diferencia_min}% menos que el más rapido')
print(f'El curso de dalto dura un {diferencia_max}% menos que el más lento')
print(
    f'El curso de dalto dura un {diferencia_promedio}% menos que el promedio')

print('----------------------------------------')

# tiempos promedio de tiempo vacio
print(f'dalto tuvo un timpo vacio promedio de {tiempo_vacio_dalto}%')
print(
    f'los demas cursos tienen un tiempo vacio promedio de {tiempo_vacio_promedio}%')

print('----------------------------------------')

# equivalencia de ver 10 horas de otros cursos y ver el curso de dalto
print(
    f'ver el curso de dalto 10 horas equivale a ver {diez_horas_dalto} de otros cursos')
print(
    f'ver 10 horas del otros cursos equivale a ver {diez_horas_promedio} del curso de dalto')

print('----------------------------------------')

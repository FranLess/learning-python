# escribir los nombre y apellidos de dos listas en un archivo .txt
nombres = ["Lucas", "Matias", "Camila", "Pedro", "Roberto"]
apellidos = ["Dalto", "Zing", "Dalto", "Robetix", "tarado"]

# registrar esta informacion en un .txt de forma optima
file_path = 'archivos_problemas\\nombres_y_apeliidos.txt'
with open(file_path, 'w') as file:
    file.writelines(['Los datos son:\n\n'])
    [file.writelines(
        [f'Nombre {name}\n',
         f'Apellido {lastname}\n',
         '--------\n']) for name, lastname in zip(nombres, apellidos)]

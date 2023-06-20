import sys
sys.path.append(
    'c:\\Users\\FcoMi\\Desktop\\main\\code\\learning_python\\')
from paquetes.paquete_saludar.saludar import saludar
from paquetes.paquete_despedir.despedir import despedir

saludo = saludar('fran')
despido = despedir('fran')
print(saludo)
print(despido)

# Funciones LAMBDA Importar modulos

import math


def area(radio):
    resultado = round(math.pi * radio * radio,2)
    print(resultado)




area(2)

area = lambda radio: round(math.pi * radio * radio,2)


print(area(2))

#¿Cómo crear y llamar funciones en Python?

"""
Crea una función que realice una suma. Para ello, tendrás que añadir dos argumentos(numero1 y numero2).
En su interior, especificarás un print() que muestre el resultado de la suma.
Deberás hacer tres llamadas que como resultado de la suma den los valores 30, 50 y 57000.
Los números que introduzcas en la llamada pueden ser los que quieras siempre que coincidan los resultados en el print().
"""

def suma(numero1,numero2):
    resultado = numero1 + numero2
    print(resultado)

suma(20,10)
suma(25,25)
suma(56999,1)




#¿Cómo utilizar *args en las funciones de Python?

#Completa el siguiente fragmento de código:

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('rojo','azul')
"""
Crea una función que realice la suma de cinco números utilizando solo *args.
Debes imprimir el resultado en la consola.
La suma no se realizará directamente sobre el print().
"""

def suma(*args)
#comentario







#¿Cómo crear un diccionario en Python?


#Del diccionario teclado2 del capítulo, muestra los elementos Modelo y Precio
#con presentación en un print(). El resultado será esto en la consola:
#El modelo Corsair K55 RGB cuesta 59,99 $.
"""
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}
teclado2['Modelo']
teclado2['Precio']

"""
"""
Del diccionario teclado2 del capítulo, muestra los elementos Modelo y Precio
con presentación en un print().
El resultado será esto en la consola:

"""
"""
#print ('El modelo' ,teclado2['Modelo'],'cuesta' ,teclado2['Precio'])

#Itera el diccionario teclado1 con un solo bucle for
#que muestre esto en la consola:
for x in teclado2:
    print(x,'=',teclado2[x])
"""
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}




    
#Metodos con diccionarios

"""
Elimina el diccionario teclado1 entero .
De teclado2 elimina las claves 'Categoría' y 'Precio'.
Muestra la última clave ('Modelo') que queda en la consola.
"""
del teclado1
del teclado2['Categoría']
del teclado2['Precio']
print(teclado2)











    

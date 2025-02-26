#¿Cómo crear un diccionario en Python?


#Del diccionario teclado2 del capítulo, muestra los elementos Modelo y Precio
#con presentación en un print(). El resultado será esto en la consola:
#El modelo Corsair K55 RGB cuesta 59,99 $.

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


print ('El modelo' ,teclado2['Modelo'],'cuesta' ,teclado2['Precio'])

#Expresiones regulares search()

import re


txt = 'fire force'

buscar = re.search("fire force", txt)

'''
como podemos observar primero creo una variable que contenga un string el que sea y
despues sobre ese texto buscare una letra que es la funcion que tiene search en ese caso seria la e
'''


print(buscar)

'''
resultado en la consola:
<re.Match object; span=(3, 4), match='e'>

tambien se puede buscar por sillabas o por palabras completas asi como frases enteras aqui un ejemplo:


'''

'''
<re.Match object; span=(5, 8), match='for'>
aqui podemos ver como encuentra la silaba y pone de que posicion a que posicion esta dicha silaba
'''

'''
aqui un ejemplo con la palabra completa:
<re.Match object; span=(5, 10), match='force'>
'''

'''
y ahora con la frase entera
re.Match object; span=(0, 10), match='fire force'
'''

#Expresiones regulares findall()

text = "en el momento adecuado"
busqueda2 = re.findall("e", text)

print(busqueda2)

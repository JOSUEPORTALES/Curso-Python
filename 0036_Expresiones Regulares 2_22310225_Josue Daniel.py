#Expresiones regulares 2


#secuencias especiales

import re

texto = "siete septimos son menos que tres siete septamos"

revel = re.findall("\Asiete",texto)
revel2 = re.findall("\D", texto)

print(revel)
#print(revel2)

#meta caracteres


revel3 = re.findall("sep..mos",texto)
revel4 = re.findall("septimos|septamos|siete",texto)
print(revel3)
print(revel4)

revel5 = re.findall("[a-m]",texto)
print(revel5)





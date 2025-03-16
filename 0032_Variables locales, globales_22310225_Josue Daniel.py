#Variables locales globales y anidadas

#varible local

def palma():
    sombra = 'Que hay de nuevo viejo'
    print(sombra)


palma()

#pero si intento llamar a la variable afuera de la funcion me marcara error debido a que es una variable local


#print(sombra)

'''
resultado del error en pantalla
Traceback (most recent call last):
  File "C:/Users/josue/Desktop/0000Inteligencia Artificial/Curso Python 2025/Curso-Python/0031_Variables locales, globales_22310225_Josue Daniel.py", line 15, in <module>
    print(sombra)
NameError: name 'sombra' is not defined

muestra que no esta definida debido a que solo exite esa variable dentro de la funcion.
'''

#Ahora veamos un ejemplo con una funcion anidada y como funcionen en esta las variables locales.


def ejercito():
    soldado1 = 'Benito'
    print(soldado1)

    def peloton():
        soldado1 = 'Presidente'
        print(soldado1)


    peloton()

ejercito()    
    
#Aqui podemos ver como la variable dentro de una fucnion anidada puede cambiar su valor sin problema.

#Ahora pondre un ejemplo de una variable global y su diferencia con variables locales

#Variable global
dia = 'Se ah hecho de noche'

def mundo():
    dia = 'Se ah hecho de dia'
    print(dia)

mundo()

print(dia)

'''
La primera variable global tiene su valor definido previamente, dentro de la funcion
este cambia el valor de la variable y luego lo imprime,
pero al imprimirlo fuera de la funcion con un print el valor que toma la variable
es el de la variable global.
'''

'''
Para acceder a una varible dentro de una fucnion solo se debe hacer las variables globales
con el comando global
ejemplo:
'''

def tiempo():
    global horas
    horas = '40 horas'

tiempo()
print(horas)



































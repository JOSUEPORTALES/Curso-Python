#bucle while

#Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.

x = 0

while x <= 15:
    print(x)
    x += 5


#Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.

x = 0

while x >= -100:
    print(x)
    x -= 20
    

#Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada ejecución esta frase con el valor de ejecución correspondiente:
#'El valor del bucle es 10'

x = 10

while x > 0:
    print('El valor del bucle es: ',x)
    x -= 1


#Crea un bucle while con las siguientes características:    
#El valor inicial de la variable x será de 0.
#El valor de incremento será 1.
#La condición de salida del bucle será mayor o igual a 30
#
#
#




x = 0

while x <= 30:
    x += 1
    
    if x == 4 or x == 6 or x == 10:
        print('Se saltó el valor ',x,'de x')
        continue
   
    if x == 15:
        print('Se rompió la ejecución del bucle cuando x valía ',x)
        break
    print('El valor del bucle es: ',x)





#Bucle FOR

#Crea un bucle for que itere la siguiente tupla y muestre una frase como esta en cada iteración:
#'El color es: ' + color + '.'.


colores = ('rojo','azul','verde','amarillo')

for x in colores:
    print('El color es: ',x,'.')

    
#Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100.
#Basta con que imprimas el valor de cada iteración.    



for x in range(7, 700, 100):
    print(x)


























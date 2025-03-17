#Fechas
import datetime

fecha = datetime.datetime.now()

print(fecha)

#Se puede mocificar la fecha quitando el time now y entre parentesis
#poner la fecha que se quiera.


fecha1 = datetime.datetime(2025,2,16)
print(fecha1)

#Tambien se puede mostrar unicamente algun dato de la fecha como lo puede ser el año
#De la siguiente manera.

print('Año: ', fecha.year)
print('Mes: ', fecha.month)
print('Dia: ', fecha.day)


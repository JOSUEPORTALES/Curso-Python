#Fechas
import datetime, locale

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


#Metodo strftime()

'''
Para este metodo la ventaja o las opciones que te da para trabajar con las fechas es que puedes tomar un valor
el que sea de la siguiente lista.
import datetime

ahora = datetime.datetime.now()

"Día de la semana abreviado: %a "))
"Día de la semana completo: %A "))
"Mes abreviado: %b "))
"Mes abreviado: %B "))
"Fecha completa: %c "))
"Siglo (empieza a contar desde cero): %C "))
"Día del mes (01 - 31): %d "))
"Día/hora/año: %D "))
"Día del mes (1 - 31): %e "))
"Año en dos dígitos: %g "))
"Año en cuatro dígitos: %G "))
"Mes abreviado: %h "))
"Hora (00 - 23): %H "))
"Hora (01 - 12): %I "))
"Día del año: %j "))
"Mes del 01 al 12: %m "))
"Minuto: %M "))
"Salto de línea: %n"))
"AM o PM: %p "))
"Hora + AM o PM: %r"))
"Hora y minutos: %R"))
"Segundos: %S"))
"Tabulación: %t"))
"Hora, minutos y segundos: %T"))
"Día de la semana (número): %u"))
"Semana del año (empieza en domingo): %U"))
"Semana del año(Condiciones especiales): %V"))
"Semana del año (empieza en lunes): %W"))
"Día de la semana (empieza en domingo): %w"))
("Día/mes/año de dos dígitos: %x"))
"Hora/minutos/segundos: %X"))
"Año corto: %y"))
"Año largo: %Y"))

'''

#La manera de usarla es la siguiente:
locale.setlocale(locale.LC_ALL, "es-ES")

date = datetime.datetime.now()

print(date.strftime("%A"))

'''
como podemos ver eleji la opcion de dia de la semana completo que corresponde al %A pero esto dependera
del tipo de dato que nesecites de una fecha.

hay un inconveniente y es que la fecha o en este caso el dia lo muestra en ingles para resolver esto solo hace
falta agregar la el modulo locale y agregar el siguiente comando.

estos son los dos resultados con y sin el locale.


'''


print(date.strftime("%Y"))











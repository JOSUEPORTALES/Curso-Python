#POO Clases
'''
class usuario:
    nombrecom = ''
    password = ''
    saldo = ''


    def imp_datos(self):
        print('Nombre:',self.nombrecom, '\nPassword:',self.password, '\nSaldo:',self.saldo)


usuario300 = usuario()
usuario300.nombrecom = 'Josue Damiel Portales Rodriguez'
usuario.password = 'pqrtE23CVnm'
usuario.saldo = '34000'


usuario300.imp_datos()
'''
'''
#Metodo _init_

class Cocina:
    def __init__(self, platillo, precio):
        self.platillo = platillo
        self.precio = precio

    def imp_datos(self):
        print('Platillo:', self.platillo, '\nPrecio:', self.precio)
        
platillo01 = Cocina('Hamburguesa','52')
platillo02 = Cocina('Hot dog' , '21')
platillo03 = Cocina('Papa rellena' , '70')

platillo01.imp_datos()
platillo02.imp_datos()
platillo03.imp_datos()


'''
#Metodo para cambiar datos de un objeto

class autopartes:
    def __init__(refaccion, numero, pieza, precio):
        refaccion.numero = numero
        refaccion.pieza = pieza
        refaccion.precio = precio

    def mostrar_datos(datos):
        print('Numero de pieza: ',datos.numero, '\nPieza: ', datos.pieza, '\nPrecio: ', datos.precio)


pieza1 = autopartes(2324,'Rin delantero',1200)
pieza2 = autopartes(2321,'Aro',600)
pieza3 = autopartes(2326,'Motor',10000)

pieza1.mostrar_datos()
pieza2.mostrar_datos()
pieza3.mostrar_datos()

pieza2.numero = 2325
pieza2.mostrar_datos()



        

#Clases vacias y eliminar objetos.

class barco:
    pass


class taller:
    def __init__(pz, sector, maquina):
        pz.sector = sector
        pz.maquina = maquina

    def mostrar_pz(lugar):
        print('Sector: ', lugar.sector, '\nMaquina: ', lugar.maquina)

maquina1 = taller(7, 'Prensadora')        
maquina1.mostrar_pz()

del maquina1.sector


maquina1.mostrar_pz()



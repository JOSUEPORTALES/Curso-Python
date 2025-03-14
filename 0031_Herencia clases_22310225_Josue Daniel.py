#Herencia de clases

class playmusic:
    def __init__(music, cancion, duracion):
        music.cancion = cancion
        music.duracion = duracion

    def view_song(rola):
        print('Cancion: ', rola.cancion, '\nDuracion: ', rola.duracion)



song1 = playmusic('Feel Good Inc','4:14')
song2 = playmusic('Deadcrush','4:59')

song1.view_song()


'''
Aqui estmos heredando los atributos y funciones que tiene la clase
padre que seria playmusic y la que esta heredando que seria la clase hijo es
playmusic_pr y se comprueba cuando creo el objeto song3 y toma los atributos
de la clase playmusic.
'''
class playmusic_pr(playmusic):
    pass

song3 = playmusic_pr('DARE','4:48')

song3.view_song()

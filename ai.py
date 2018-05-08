from random import randrange


def tah_pocitace(pole, znak='o'):
    #Vygeneruje náhodné políčko, zkontoluje obsazenost a hraje
    policko=randrange(0,len(pole)+1)
    while pole[policko] != '-':         #ošetřuje zahrání na už obsazené pole
        print('Znova')
        policko=randrange(0,20)
    pole1 = pole[0:policko]             #samotný tah, šlo by vytáhnout do funkce tah
    pole2 = pole[policko+1:]
    pole = pole1 + znak + pole2
    return pole

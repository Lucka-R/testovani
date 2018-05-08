from random import randrange
from ai import tah_pocitace


pole = '--------------------'
policko = ''
znak = ''
vyhra = '-'

def tah_hrace(pole, policko):
    #vyhodnotí správnost čísla input políčka a zda políčko není plné
    #Pokud je, požádá o input znovu
    #pokud není, zaznamená tah
    znak='x'                                                      #tady chce doladit neelegantní řešení znaku
    while policko not in range(0,len(pole)+1):
        print('Neplatné číslo políčka. Zadej číslo od 0 do 19')
        policko=int(input('Na které políčko chceš hrát?'))

    while pole[policko] != '-':
        print('Policko uz je zabrane. Zkus jine!')
        policko=int(input('Na které políčko chceš hrát?'))

    pole1 = pole[0:policko]
    pole2 = pole[policko+1:]
    pole = pole1 + znak + pole2
    return pole


def vyhodnot_stav(pole):
    if '-' not in pole:
        vyhra = '!'
    elif 'ooo' in pole:
        vyhra = 'o'
    elif 'xxx' in pole:
        vyhra = 'x'
    else:
        vyhra = '-'
    return vyhra

def main():
    global vyhra
    global pole
    while vyhra == '-':
        policko=int(input('Na které políčko chceš hrát? (0-19)'))
        pole=tah_hrace(pole, policko)

        print(pole)
        print('teď hraje počítač')

        pole=tah_pocitace(pole)
        print (pole)

        vyhra = vyhodnot_stav(pole)
        print(vyhra)

    vyhra = vyhodnot_stav(pole)
    if vyhra == '!':
        print ('Remíza')
    elif vyhra == 'x':
        print ('Vyhrál jsi!')
    elif vyhra == 'o':
        print ('Vyhrál počítač!')
    else:
        print ('Máš kód na houby a koukej si tam najít chybu') # kontrolní řádka pro mě

import tkinter
import threading
import random
import time
######################################################


def nacitaj_mapu(cesta):
    # vytvorime cestu k suboru, ktory budeme pouzivat
    subor = open('textak.txt')
    # z prveho riadku v subore nacitame sirku

    sirka = int(subor.readline())
    # z druheho riadku v subore nacitame vysku

    #celysubor = subor.readlines()
    #vyska = int(celysubor[0]) .... tento sposob mi nefungoval tak som to skusal s cislom kym mi to nevyjde spravit uplne cele co sa nakoniec nepodarilo
    vyska = 10

    # vytvorime premennu mapa, ktora je zoznam - list
    mapa = []

    # pre kazdy riadok mapy precitaj kazdy riadok a vytvor z nich zoznam (rozsah je po vysku)
    for y in range(0, 11):
        line = subor.readlines()
        mapa.append(list(line))

    subor.close()

    return sirka, vyska, mapa

# uzavri subor

# tieto hodnoty nam vrati z funkcie

######################################################

def vytvor_platno(okno, sirka, vyska, mapa, cell_size, wall):
    platno = tkinter.Canvas(okno, width = sirka*cell_size, height = vyska *cell_size)
    platno.config(bg='cyan')
    platno.pack()

    # ak je polozka v poli rovna #, tak vytvor obrazok pre stenu (rozsah je po vysku, resp sirku)
    for y in range(0, vyska):
        for x in range(0, sirka):
            if mapa[y][x] == '#':
                platno.create_image(x * cell_size + cell_size / 2, y * cell_size + cell_size / 2,  image = wall)

            # vrati nakreslene platno
            return platno

######################################################

# mapa - steny a prechody (1. index - vyska, 2. index sirka)
mapa = []

# rozmery mapy
sirka = 20
vyska = 0

# rozmer policka (px)
cell_size = 80

######################################################

okno = tkinter.Tk()
okno.title('bludisko')

# nacitaj zo suboru mapu a vratene hodnoty uloz do premennych.
# vsetky nazvy premennych sesdia s lokalnymi premennymi, ale nie su to totozne
# premenne.

sirka, vyska, mapa = nacitaj_mapu('textak.txt')

# obrazok si musime odlozit v premennej, ktora prezije platno a preto je globalna
wall = tkinter.PhotoImage(file='wall.gif')

# volame funkciu vytvor_platno tak, ze ju priradime do premennej. v zatvorke musia byt nazvy vsetkych premennych, ktore potrebuje na inicializaciu
platno = vytvor_platno(okno, sirka, vyska, mapa, cell_size, wall)

okno.mainloop()
terminate = True

# ulohu sa mi stopercentne spravit nepodarilo, a tak posielam aspon to co som zvladol
import tkinter
import threading
import random
import time


####################################

def nacitaj_mapu():
    txt = open("textak.txt")
    sirka = int(txt.readline())
    vyska = int(txt.readline())
    mapa = []

    pac_found = False
    duch_found = False


    for i in range(0, vyska):
        riadok = txt.readline()
        mapa.append(riadok)

    txt.close()

    for y in range(0, vyska):
        if pac_found == True and duch_found == True:
         break;
        for x in range(0, sirka):
            if mapa[y][x] == 'p':
                mapa[y][x] == 'p'
                pac_x = x
                pac_y = y
                pac_found = True

            elif mapa[y][x]='d':
                mapa[y][x] = ''
                duch_x = x
                duch_y = y
                duch_found = True

            if pac_found and duch_found:
                break;



    return sirka, vyska, mapa, pac_x, pac_y, duch_x, duch_y


####################################

def vytvor_platno(okno, sirka, vyska, mapa, cell_size, wall):
    platno = tkinter.Canvas(okno, \
                            width=sirka * cell_size, \
                            height=vyska * cell_size)
    platno.config(bg="cyan")
    platno.pack()

    for y in range(0, vyska):
        for x in range(0, sirka):
            if mapa[y][x] == '#':
                # co je [y] [x]???
                platno.create_image(x * cell_size + sirka / 2, \
 \
                                    y * cell_size + vyska / 2, \
 \
                                    image=wall)
    ##vrati sa nam nakreslene platno
    return platno

#######################################

def panacikmove(event):
    global pac_x
    global pac_y
    global platno
    global pacman
    global cell_size
    global mapa
    global skore
    global gulicky
    global okno

    target_x = pac_x
    target_y = pac_y

    if event.keysym == 'Up':
        target_y -= 1
    elif event.keysym == 'Down':
        target_y += 1
    elif event.keysym == 'Left':
        target_x -= 1
    elif event.keysym == 'Right':
        target_x += 1

    if mapa[target_y][target_x] != '':
        pac_x = target_x
        pac_y = target_y

        platno.coords(pacman, target_x * cell_size + cell_size/2, target_y * cell_size + cell_size/2)
        global duch_x
        global duch_y

####################################

# mapa - steny a prechody (1. index - vyska, 2. index sirka)
mapa = []

# rozmery mapy
siroka = 20
vysoka = 0

# rozmery policla v px
cell_size = 80

####################################

okno = tkinter.Tk()
okno.title("hrafilip")

# nacitaj zo suboru mapu a vratane hodnoty uloz do premennych
# vsteky nazvy premennych sedia s lokalnymi premennymi, ale nie su to
# totozne premenne

sirka, vyska, mapa = nacitaj_mapu()

# obrazok si musime odlozit v premennej, ktora prezije platno a preto
# je globalna

wall = tkinter.PhotoImage(file="wall.gif")

# volame funkciu vytvor_platno tak, ze ju priradime do premennej
# v zatvorke musia byt nazvy vsetkych premennych, ktore potrebujeme
# na inicializaciu

platno = vytvor_platno(okno, sirka, vyska, mapa, cell_size, wall)

okno.mainloop()
terminate = True

print("O")
import tkinter
import threading
import random
import time
####################################

def nacitaj_mapu():
    txt = open(file = 'textak.txt.txt')
    sirka = int(txt.readline())
    vyska = int(txt.readline())
    mapa = []

    panacik_found = False
    duch_found = False

    for i in range(0, vyska):
        riadok = txt.readline()
        mapa.append(list(riadok))

    txt.close()

    for y in range(0, vyska):
        if panacik_found == True and duch_found == True:
         break;
        for x in range(0, sirka):
            if mapa[y][x] == 'p':
                mapa[y][x] == ' '
                panacik_x = x
                panacik_y = y
                panacik_found = True

            elif mapa[y][x]=='d':
                mapa[y][x] == ' '
                duch_x = x
                duch_y = y
                duch_found = True

            if panacik_found == True and duch_found == True:
                break;

    return sirka, vyska, mapa, panacik_x, panacik_y, duch_x, duch_y

def vytvor_peniaz(platno, sirka, vyska, mapa, cell_size):
    peniaze = []
    for y in range(0, vyska):
        for x in range(0, sirka):
            if mapa[y][x] == 'm':
                obr = platno.create_image(x * cell_size + cell_size/2, y * cell_size + cell_size/2, image = peniaz_data)
                peniaze.append([x, y, obr])
    return peniaze

#def vytvor_ducha(platno, sirka, vyska, mapa, cell_size):
    #duchovia = []
    #for y in range(0, vyska):
        #for x in range(0, sirka):
            #if mapa[y][x] == 'd':
                #obr1 = platno.create_image(x * cell_size + cell_size/2, y * cell_size + cell_size/2, image = duch_data)
                #duchovia.append([x, y, obr1])
    #return duchovia

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
                platno.create_image(x * cell_size + cell_size / 2, \
 \
                                    y * cell_size + cell_size / 2, \
 \
                                    image=wall)
    ##vrati sa nam nakreslene platno
    return platno

#######################################

def panacikmove(event):
    global panacik_x
    global panacik_y
    global platno
    global pacman
    global cell_size
    global mapa
    global skore
    global gulicky
    global okno
    global duch

    target_x = panacik_x
    target_y = panacik_y

    if event.keysym == 'Up':
        target_y -= 1
        platno.move(duch, 40, 40)
    elif event.keysym == 'Down':
        target_y += 1
        platno.move(duch, 40, 40)
    elif event.keysym == 'Left':
        target_x -= 1
        platno.move(duch, 40, 40)
    elif event.keysym == 'Right':
        target_x += 1
        platno.move(duch, 40, 40)

    if mapa[target_y][target_x] != '#':
        panacik_x = target_x
        panacik_y = target_y

        platno.coords(panacik, target_x * cell_size + cell_size/2, target_y * cell_size + cell_size/2)
    global duch_x
    global duch_y

####################################

# mapa - steny a prechody (1. index - vyska, 2. index sirka)
mapa = []

# rozmery mapy
sirka = 20
vyska = 0

panacik_x = 0
panacik_y = 0

duch_x = 0
duch_y = 0

# rozmery policla v px
cell_size = 80

####################################

okno = tkinter.Tk()
okno.title("hrafilip")


sirka, vyska, mapa, panacik_x, panacik_y, duch_x, duch_y = nacitaj_mapu()


peniaz_data = tkinter.PhotoImage(file = 'peniaz.gif')
wall = tkinter.PhotoImage(file="wall.gif")
duch_data = tkinter.PhotoImage(file = 'iababy.gif')

platno = vytvor_platno(okno, sirka, vyska, mapa, cell_size, wall)
peniaze = vytvor_peniaz(platno, sirka, vyska, mapa, cell_size)
#duchovia = vytvor_ducha(platno, sirka, vyska, mapa, cell_size)

panacik_data = tkinter.PhotoImage(file = 'shrek.gif')
panacik = platno.create_image(panacik_x * cell_size + cell_size / 2, panacik_y * cell_size + cell_size / 2, image = panacik_data)

#duch_data = tkinter.PhotoImage(file = 'iababy.gif')
duch = platno.create_image(duch_x * cell_size + cell_size / 2, duch_y * cell_size + cell_size / 2, image = duch_data)


#def duchmove(event):
    #if event.keysym == 'Up' or event.keysym == 'Down' or event.keysym == 'Left' or event.keysym == 'Right':
        #platno.move(duch, -15, 15)

duch_smer = 3
terminate = False

platno.bind_all ('<KeyPress-Up>', panacikmove)
platno.bind_all ('<KeyPress-Down>', panacikmove)
platno.bind_all ('<KeyPress-Left>', panacikmove)
platno.bind_all ('<KeyPress-Right>', panacikmove)

platno.bind_all ('<KeyPress-Escape>', lambda key: okno.destroy())

okno.mainloop()
terminate = True
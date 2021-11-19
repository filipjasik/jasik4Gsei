from tkinter import *
from random import randrange, uniform
okno = Tk()
platno = Canvas(okno, width=1000, height=1000)
platno.pack()

faza1 = PhotoImage(file="emmkahop1.gif")
init_img = platno.create_image(700,400, anchor=NW, image=faza1)
faza2 = PhotoImage(file="emmkahop2.gif")
faza3 = PhotoImage(file="emmkahop3.gif")



def pankohop(event):
    f = randrange(0,3)
    if f == 0:
        platno.itemconfig(init_img, image=faza2)
    elif f == 1:
        platno.itemconfig(init_img, image=faza3)
    elif f == 2:
        platno.itemconfig(init_img, image=faza1)
    if event.keysym == 'Up':
        platno.move(1, 0, -10)
    elif event.keysym == 'Down':
        platno.move(1, 0, 10)
    elif event.keysym == 'Left':
        platno.move(1, -10, 0)
    else:
        platno.move(1, 10, 0)

platno.bind_all('<KeyPress-Up>', pankohop)
platno.bind_all('<KeyPress-Down>', pankohop)
platno.bind_all('<KeyPress-Left>', pankohop)
platno.bind_all('<KeyPress-Right>', pankohop)

mainloop()
input()
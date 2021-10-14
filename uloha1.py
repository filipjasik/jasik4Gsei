from tkinter import *
import random
okno = Tk()
platno = Canvas(okno, width = 500, height = 500)
platno.pack()

obdlznik = platno.create_rectangle(10, 10, 20, 40)

for a in range(0, 100):
    w = random.randrange(50)
    h = random.randrange(20)
    a = platno.create_rectangle(w,h)


input()


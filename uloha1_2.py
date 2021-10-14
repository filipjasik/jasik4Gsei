from tkinter import *
import random
okno = Tk()
platno = Canvas(okno, width = 800, height = 800)
platno.pack()

def obdlznik(width, height):
    x1 = random.randrange(0, 800)
    y1 = random.randrange(0, 800)
    x2 = 30 + int(x1)
    y2 = 50 + int(y1)
    platno.create_rectangle(x1, y1, x2, y2)

for a in range(0, 100):
    obdlznik(800, 800)

input()
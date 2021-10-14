from tkinter import *
import time
okno = Tk()

platno = Canvas(okno, width = 500, height = 500)
platno.pack()

trojuholnik = platno.create_polygon(20, 20, 60, 20, 60, 60)



for x in range(1,100):
    platno.move(1, 8, 8)
    #animovat utvar
    okno.update ()
    time.sleep(0.05)
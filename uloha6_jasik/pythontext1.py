from tkinter import *
#uloha1:
#textsubor = open('text1.txt')

#uloha2:
#citacka = textsubor.read()
#print(citacka)

#uloha3:
#riadok1 = (textsubor.readline())
#print(riadok1)

#uloha4:
#textsubor = open('text1.txt', 'w')
#pridat = textsubor.write('vidime sa znova')
#textsubor.close()

#uloha5:
#znaky = textsubor.read()
#pocetznakov = len(str(znaky))
#print(pocetznakov)

#uloha6:
okno = Tk()
okno.geometry('1000x1000')

textsubor = open('cloud.txt')
citacka2 = textsubor.read()

text = Text(okno)
def nacitat():
    vytlacit = Label(text = citacka2, font = 10).pack()

tlacitko = Button(okno, text = 'klikni sem', command=nacitat)
tlacitko.pack()

textsubor.close()
okno.mainloop()

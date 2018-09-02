# Графическая оболочка лифта
from tkinter import *

root = Tk()
root.title("Лифт")
root.geometry("400x300+300+250")        #Ширина и высота (окна)

Knopka_1 = Button(text="1 этаж")        #Создание кнопок и их атрибутов
Knopka_2 = Button(text="2 этаж")
Knopka_3 = Button(text="3 этаж")
Knopka_4 = Button(text="4 этаж")
Knopka_5 = Button(text="5 этаж")
Knopka_6 = Button(text="6 этаж")
Knopka_7 = Button(text="7 этаж")
Knopka_8 = Button(text="8 этаж")
Knopka_9 = Button(text="9 этаж")
x=10
Knopka_nomer = Button(text=x)

Knopka_1.place(x=0,y=200)               #Размещение кнопок и привязка к функциям
Knopka_2.place(x=0,y=175)
Knopka_3.place(x=0,y=150)
Knopka_4.place(x=0,y=125)
Knopka_5.place(x=0,y=100)
Knopka_6.place(x=0,y=75)
Knopka_7.place(x=0,y=50)
Knopka_8.place(x=0,y=25)
Knopka_9.place(x=0,y=0)
Knopka_nomer.place(x=200,y=0)
root.mainloop()                         #Цыкл событий
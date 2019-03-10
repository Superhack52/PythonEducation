from tkinter import *
root = Tk()
root.title("Бесполезные кнопки")
root.geometry("300x85")
app = Frame(root)
app.grid()
#создание кнопки внутри рамки
bttn1 = Button(app, text = "Я ничего не делаю!")
bttn1.grid()
bttn2 = Button(app)
bttn2.grid()
bttn2.config(text ="И я тоже!")
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "И я!"
root.mainloop()

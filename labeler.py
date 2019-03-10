from tkinter import *
root = Tk()
root.title("Это я, метка")
root.geometry("200x50")
#внутри окна создается рамка для размещения других элементов
app = Frame(root)
app.grid()
#Создание метки внутри рамки
lbl = Label(app, text = "Вот она я!")
lbl.grid()
root.mainloop()
from tkinter import *
class Application(Frame):
    """GUI-приложение с тремя кнопками"""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Создает три бесполехных кнопки """
        self.bttn1 = Button(self, text = "Я ничего не делаю!")
        self.bttn1.grid()
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "И я тоже!")
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "И я!"

root = Tk()
root.title("Бесполезные кнопкик - 2")
root.geometry("350x85")
app = Application(root)
root.mainloop()
#применение переключателей
from tkinter import *
class Application(Frame):
    """GUI-приложение, выбрать жанры кино."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """Элементы, чтобы выбирать"""
        Label(self, text = "Укажите ваш любимый жанр кино:").grid(row = 0, column = 0, sticky = W)
        Label(self, text = "Выберите ровно один:").grid(row = 1, column = 0, sticky = W)
        #переменная для хранения выбранного жанра
        self.favorite = StringVar()
        self.favorite.set(None)
        #комедия
        Radiobutton(self,
        text = "Комедия",
        variable = self.favorite,
        value = "комедия",
        command = self.update_text
        ).grid(row = 2, column = 0, sticky = W)
        Radiobutton(self,
        text = "Драма",
        variable = self.favorite,
        value = "драма",
        command = self.update_text
        ).grid(row = 3, column = 0, sticky = W)
        Radiobutton(self,
        text = "Кино о любви",
        variable = self.favorite,
        value = "кино о любви",
        command = self.update_text
        ).grid(row = 4, column = 0, sticky = W)
        #текстовая область с результатом
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)
    def update_text(self):
        message = "Ваш любимый киножанр - "
        message += self.favorite.get()
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

root = Tk()
root.title("Киноман-2")
app = Application(root)
root.mainloop()
#применение флажков
from tkinter import *
class Application(Frame):
    """GUI-приложение, выбрать жанры кино."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """Элементы, чтобы выбирать"""
        Label(self, text = "Выберите все, что вам по вкусу:").grid(row = 1, column = 0, sticky = W)
        #флажок комедия
        self.likes_comedy = BooleanVar()
        Checkbutton(self,
        text = "Комедия",
        variable = self.likes_comedy,
        command = self.update_text
        ).grid(row = 2, column = 0, sticky = W)
        #флажок "Драма"
        self.likes_drama = BooleanVar()
        Checkbutton(self,
        text = "Драма",
        variable = self.likes_drama,
        command = self.update_text
        ).grid(row = 3, column = 0, sticky = W)
        #флажок "Фильм о любви"
        self.like_romance = BooleanVar()
        Checkbutton(self,
        text = "Фильм о любви",
        variable = self.like_romance,
        command = self.update_text
        ).grid(row = 4, column = 0, sticky = W)
        #текстовая область с результатом
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)
    def update_text(self):
        """Обновление текстового элемента по мере выбора"""
        likes = ""
        if self.likes_comedy.get():
            likes += "Вам нравятся комедии.\n"
        if self.likes_drama.get():
            likes += "Драма.\n"
        if self.like_romance.get():
            likes += "Кино о любви.\n"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)

root = Tk()
root.title("Киноман")
app = Application(root)
root.mainloop()


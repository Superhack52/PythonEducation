#Демонстрация текстового поля, текстовой области и менеджер размещения Grid
from tkinter import *
class Application(Frame):
    """GUI-приложение, владеющая секретом долголетия."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """Создает кнопку, текстовое поле и текстовую область"""
        #метка инструкция
        self.inst_lbl = Label(self, text = "Чтобы узнать секрет долголетия, введите пароль")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        #метка около ввода пароля
        self.pw_lbl =  Label(self, text = "Пароль:")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)
        #текстовое поле для ввода пароля
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)
        #кнопака отправки значения
        self.submit_button = Button(self, text = "Узнать секрет", command = self.reveal)
        self.submit_button.grid(row = 2, column = 0, sticky = W)
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)
    def reveal(self):
        """В зависимости от введенного пароля отвечает разными сообщениям."""
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "Правильно"
        else:
            message = "Неправильно"
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)

root = Tk()
root.title("Долгожитель")
root.geometry("300x150")
app = Application(root)
root.mainloop()
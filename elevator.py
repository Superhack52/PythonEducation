#Лифт
from tkinter import *
from tkinter import messagebox

class Elevator():
    def __init__(self):
        self.__currentFloor = 0
    def move_to(self, targetFloor):
        if targetFloor > self.__currentFloor:
            self.__move(targetFloor, True)
        elif targetFloor < self.__currentFloor:
            self.__move(targetFloor, False)
        else:
            self.__printMessage("Лифт на нужном этаже!")
    def __move(self, targetFloor, up):
        direction = up and "вверх" or "вниз"
        message = ""
        while self.__currentFloor != targetFloor:
                line = "Лифт едет " + str(direction) + ". " + str(self.__currentFloor) + "\n"
                message += line
                if up:
                    self.__currentFloor += 1
                else:
                    self.__currentFloor -= 1
        message += "Лифт остановился на этаже " + str(self.__currentFloor)
        self.__printMessage(message)
    def __printMessage(self, message):
        messagebox.showinfo("Движение лифта", message)

def click_button():                         
    global elevatorTest
    global floor
    elevatorTest.move_to(floor.get())

elevatorTest = Elevator()

root = Tk()
root.title("Лифт")
root.geometry("300x250")

floor = IntVar()
message_entry = Entry(textvariable=floor)
message_entry.place(relx=.5, rely=.1, anchor="c")
btn = Button(text="Me", background="#555", foreground="#ccc",
             padx="10", pady="15", font="3", command=click_button)
btn.pack()
btn.place(relx=.10, rely=.1)
root.mainloop()
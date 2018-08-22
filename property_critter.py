#Демонстрация свойства
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверюшки не может быть пустой строкой.")
        else:
            self._name = new_name
            print("Имя успешно изменено.")
    def talk(self):
        print("\nПривет, меня зовут", self.name)
crit = Critter("Бобик")
crit.talk()
print("\nМою зверушку зовут", end = " ")
print(crit.name)
print("\nИзменения имени зверушки на Мурзик...")
crit.name = "Мурзик"
print("Мою зверушку зовут", end = " ")
print(crit.name)
print("\nПопытка изменить имя на пустую строку...")
crit.name = ""
print("Мою зверушку зовут", end = " ")
print(crit.name)
input("\nНажмите Enter, чтобы выйти.")

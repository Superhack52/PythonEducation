# Демонстрирует атрибуты класса и статические методы
class Critter(object):
    """Виртуальныя питомец"""
    total = 0
    @staticmethod
    def status():
        print("\nВсего зверюшек сейчас", Critter.total)
    def __init__(self, name):
        print("Появилась на свет новая зверушка!")
        self.name = name
        Critter.total += 1
print("Атрибут total =", Critter.total)
print("\nСоздание зверушек")
crit1 = Critter("зверушка 1")
crit2 = Critter("зверушка 2")
crit3 = Critter("зверушка 3")
Critter.status()
print("Снова total =", crit1.total)
input("\nPress enter...")

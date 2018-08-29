#Сундук
class Chest(object):
    """Сундук"""
    def __init__(self):
        self.__thing = Goods.GetRandomThing()
        self.__isOpened = False
        self.__isClear = False
    def Open(self):
        if self.__isOpened:
            print("Сундук уже открыт!")
        else:
            print("Сундук открывается и в нем лежит:", self.__thing)
    def GetThing(self):
        if self.__isClear:
            print("Сундук пуст!")
        else:
            thingToReturn = self.__thing
            self.__thing = None
            return thingToReturn
class Goods(object):
    GOODS_LIST = {"Щит","Меч", "Булава", "Кирка","Броня" ,"И так далее"}
    @staticmethod
    def GetRandomThing():
        if Goods.GOODS_LIST:
            import random
            index = random.randint(0,len(Goods.GOODS_LIST) - 1)
            thing = Goods.GOODS_LIST[index]
            del Goods.GOODS_LIST[index]
            return thing
def Main():
    firstChest = Chest()
    firstChest.Open()
    thing = firstChest.GetThing()
    print("Мы получили из сундука - ", thing)
Main()

input("\n\nНажмите Enter, чтобы закрыть приложение.")
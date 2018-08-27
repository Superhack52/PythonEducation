class ChestFactory(object):
    __GOODS = ["Щит","Меч", "Булава", "Кирка","Броня" ,"И так далее"]
    class Chest(object):
        def __init__(self, thing):
                self.__thing = thing
                self.__isOpened = False
                self.__isEmpty = False
        def Open(self):
            if self.__isOpened: 
                if not self.__isEmpty:
                    print("Сундук уже открыт. В нем лежит -", self.__thing)
                else:
                    print("Сундук пуст!")
            else:
                self.__isOpened = True
                print("Сундук открывается и в нем лежит -", self.__thing)
        def Get(self):
            content = self.__thing
            print("Вы забираете", content, "из сундука.")
            self.__thing = None
            self.__isEmpty = True
            return content
        def __str__(self):
            return "Сундук. В нем лежит" + " " + self.__thing      
    @staticmethod
    def GetChest():
        import random
        index = random.randint(0, len(ChestFactory.__GOODS) - 1)
        return ChestFactory.Chest(ChestFactory.__GOODS[index])
chestOne = ChestFactory.GetChest()
chestOne.Open()
goodFromChest = chestOne.Get()
chestOne.Open()
input("\nНажмите Enter.")
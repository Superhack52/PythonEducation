#Демонстрация взаимодействия объектов
class Player(object):
    """Игрок в игре"""
    def blast(self, enemy):
        print("Игрок стреляет во врага.\n")
        enemy.die()
class Alien(object):
    """Враг в игре"""
    def die(self):
        print("Враг убит.\n")
#main
print("\tГибель пришельца\n")
hero = Player()
invaider = Alien()
hero.blast(invaider)
input("\nPress enter to exit.")
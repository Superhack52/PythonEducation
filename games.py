#Демонстрирует создание модулей
class Player():
    """Участник игры"""
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return self.name + ":\t" + str(self.score)
def ask_yes_no(question):
    """Задает вопрос с ответом 'да' или 'нет'"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response
def ask_number(question, low, high):
    """Просит ввести число из заданного диапазона."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
if __name__ == "__main__":
    print("Вы запустили этот модуль напрямую, а не импортировали его.")
    input("\nНажмите Enter, чтобы выйти.")
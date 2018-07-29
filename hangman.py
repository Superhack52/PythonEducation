#Виселица
#Выбирает случайное слово. Игрок должен угадать за отведенное количество попыток.
import random
HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O  |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O  |  -+-
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O  |  /-+-
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O  |  /-+-/
     |    |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O  |  /-+-/
     |    |
     |    |
     |   |
     |   |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O  |  /-+-/
     |    |
     |    |
     |   | |
     |   | |
     |
    ----------
    """)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("КНИГА", "ЛОШАДЬ", "НОУТБУК", "ЦИКЛ", "СОЛНЦЕ")
#инициализация пременных
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0 #количество ошибок, который сделал игрок
used = [] #буквы, которые игрок уже предлагал
print("Добро пожаловать в игру 'Виселица'.")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nВы уже предлагали следующие буквы:\n", used)
    print("\nОтгаданное вами в слове сейчас выглядит так:\n", so_far)
    guess = input("\n\nВведите букву: ")
    guess = guess.upper()
    while guess in used:
        print("\nВы уже предлагали букву", guess)
        guess = input("\n\nВведите букву: ")
        guess = guess.upper()
    used.append(guess)
    if guess in word:
        print("\nДа! Буква", guess, "есть в словаре!")
        #новая строка so_far с отгаданной буквой или буквами
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nК сожалению, буквы", guess, "нет в слове.")
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nВас повесили")
else:
    print("\nВы отгадали!")
print("\nБыло задано слово", word)
input("\n\nНажмите Enter, чтобы выйти")
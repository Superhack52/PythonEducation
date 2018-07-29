# Переводчик
# Демонстрирует использование словарей
geek = {"404": "Не знать, не владеть инофрмацией",
        "Googling": "'Гугление', поиск в Свети сведений о ком-либо",
        "Keybord Plaque": "Мусор, который скапливает в клавиатуре компьютера"}
choice = None
while choice != "0":
    print(
        """
        Переводчик
        0 - Выйти
        1 - Найти толковвание термина
        2 - Добавить термин
        3 - Изменить толкование
        4 - Удалить термин
        """
    )
    choice = input("Ваш выбор: ")
    print()
    #Exit
    if choice == "0":
        print("Досвидание")
    elif choice == "1":
        term = input("Какой термин вы хотите перевести? ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "означает", definition)
        else:
            print("\nУвы, этото термин мне не знаком:", term)
    elif choice == "2":
        term = input("Какой термин вы хотите добавить? ")
        if term not in geek:
            definition = input("\nВпишите ваше толкование: ")
            geek[term] = definition
            print("\nТермин", term, "добавлен в словарь")
        else:
            print("\nТакой термин уже есть! Попробуйте изменить его толкование.")
    elif choice == "3":
        term = input("Какой термин вы хотите переопределить? ")
        if term in geek:
            definition = input("\nВпишите ваше толкование: ")
            geek[term] = definition
            print("\nТермин", term, "переопределен.")
        else:
            print("\nТакого термина пока нет! Попробуйте добавить его в словарь.")
    elif choice == "4":
        term = input("Какой термин вы хотите удалить? ")
        if term in geek:
            del geek[term]
            print("\nТермин", term, "удален.")
        else:
            print("\nТермина", term, "нет в словаре.")
    else:
        print("Извините, в меню нет пункта. ", choice)
input("\nНажмите Enter, чтобы выйти...")
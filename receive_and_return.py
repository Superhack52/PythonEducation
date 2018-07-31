def display(message):
    print(message)
def give_me_five():
    five = 5
    return five
def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response
display("Вам сообщение.\n")
number = give_me_five()
print("Вот что возвращает функция give_me_five:", number)
answer = ask_yes_no("\nПожалуйства, введите 'y' или 'n': ")
print("Спасибо, что ввели:", answer)
input("\n\nНажмите Enter, чтобы выйти.")
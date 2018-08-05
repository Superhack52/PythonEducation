# Демонстрация обработки исключительных ситуаций
try:
    num = float(input("Введите число: "))
except:
    print("Похоже, это не число!")
# Конкретное исключение
try:
    num = float(input("Введите число: "))
except ValueError:
    print("Это не число!")
# Обработка исключений нескольких разных типов
print()
for value in (None, "Привет!"):
    try:
        print("Попытка преобразовать в число: ", value, "->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Похоже, это не число!")
print()
for value in (None, "Привет!"):
    try:
        print("Попытка преобразовать в число: ", value, "->", end=" ")
        print(float(value))
    except (TypeError):
        print("Можно преобразовать только строки в числа!")
    except (ValueError):
        print("Можно преобразовать только строки, состоящие из цифр!")
# Получение аргумента
try:
    num = float(input("\nВведите число: "))
except ValueError as e:
    print("Это не число! Интерпретатор говорит: ")
    print(e)
# try/exception/else
try:
    num = float(input("\nВведите число: "))
except ValueError:
    print("Это не число!")
else:
    print("Вы ввели число ", num)
input("\nPress enter to exit.")
#Work with global variables
def read_global():
    print("Значение глобальной переменной", value)
def shadow_global():
    value = -10
    print("В области видимости shadow_global", value)
def change_global():
    global value
    value = -10
    print("В области видимости global_change", value)

value = 10
print("В глобальной области видимости значение", value)
read_global()
print("Снова в глобальной", value)
shadow_global()
print("Опять в глобальной", value)
change_global()
print("И в последний раз", value)
read_global()
input("\nНажмите Enter, чтобы выйти...")

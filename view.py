import sys

def input_num(text):
    while True:
        try:
            num = int(input(text))
            return num
        except:
            print("Введите число!")


def user_exit():
    print("Вернуться в меню? Y/N ")
    userIn = input(">> ")
    if userIn in list("YyНн"):
        return True
    else:
        sys.exit()


def show_menu():

    print("Выберите команду:\n\n1 - показать всех сотрудников\n2 - добавить сотрудника\n3 - изменить данные сотрудника"
          "\n4 - удалить сотрудника\n5 - экспорт в txt\n6 - импорт из txt\n7 - импорт из csv\n0 - Выход")

    while True:

        try:
            userIn = input_num(">> ")
            if userIn in range(0, 8):
                return userIn

        except ValueError:

            print("Попробуйте ввести одно из предложенных чисел!")



def show_employes(spisok):
    print("Список всех сотрудников")
    for i, sotrudnik in enumerate(spisok):
            print(i + 1, *sotrudnik)


def add_emloyees():
    print("Введите Фамилию Имя Телефон и Должность через пробел: ")
    data = input().split()
    return data


def update_employee():
    while True:
        try:
            change = int(input("Введите номер строки для перезаписи и нажмите Enter: "))
            lst = input("Введите строку, которую хотите перезаписать. Порядок полей:\n"
                           "Фамилия Имя Телефон Должность (разделитель между полями - пробел) ").split()
            return change, lst

        except ValueError:
            print("Сначала номер строки!")




def delete():
    print("Введие номер строки для удаления ")
    number = int(input())
    return number
import csv

def get_list():
    with open('file.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        return list(reader)


def add_emloyee_to_list(employee):
    with open('file.csv', 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(employee)


def update_employe(number, lst):
    flag = True
    while flag:
        try:
            with open('file.csv', 'r', encoding="utf8", newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                data = list(reader)
                data[number] = lst
                print("Отладка", data[number])
                print("Отладка", data)

            with open('file.csv', 'w', encoding="utf8", newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=";")
                for i in data:
                    writer.writerow(i)
            flag = False

        except IndexError:
            print("Попробуйте снова!")
            flag = False


def delete(number):
    with open('file.csv', 'r', encoding="utf8", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader)
        del data[number]
    with open('file.csv', 'w', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for i in data:
            writer.writerow(i)


def export_list_txt():
    with open('file.csv', 'r', encoding="utf8", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        list_employees = list(reader)
    with open('list-employees.txt', 'w', encoding="utf-8") as data:
        for i in list_employees:
            for j in i:
                data.write(j + ' ')
            data.write('\n')


def import_list_txt():
    with open('list-employees.txt', 'r', encoding='utf-8') as data:
        for row in data:
            print(row)


def import_list_csv():
    with open("file.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=";")
        count = 0
        for row in file_reader:
            if count == 0:
                print(f'Информация по следующим столбцам:\n {", ".join(row)}')
            print(f' {row["Фамилия"]} {row["Имя"]}, {row["Телефон"]}, {row["Должность"]}')
            count += 1
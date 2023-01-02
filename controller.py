import model
import view
import logging

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    encoding='utf-8',
                    level=logging.INFO)


def main():
    while True:

        userIn = view.show_menu()

        if userIn == 1:
            logging.info("Выбран просмотр списка сотрудников")
            employee = model.get_list()
            view.show_employes(employee)
            logging.info("Показан список сотрудников")
            view.user_exit()

        elif userIn == 2:
            logging.info("Выбрано добавление сотрудника")
            data = view.add_emloyes()
            model.add_emloey_to_list(data)
            logging.info("Сотрудник добавлен")
            view.user_exit()

        elif userIn == 3:
            logging.info("Выбрано изменить запись")
            change, string = view.update_emploey()
            print(change, string)
            model.update_employe(change, string)
            logging.info("Изменения внесены")
            view.user_exit()

        elif userIn == 4:
            logging.info("Выбрано удаление сотрудника")
            number = view.delete()
            model.delete(number)
            logging.info("Сотрудник удален")
            view.user_exit()

        elif userIn == 5:
            logging.info("Выбран экспорт в txt")
            model.export_list_txt()
            logging.info("Список сотрудников экспортирован в корневой каталог программы")
            view.user_exit()

        elif userIn == 6:
            logging.info("Выбран импорт из txt")
            model.import_list_txt()
            logging.info("Список сотрудников из txt импортирован")
            view.user_exit()

        elif userIn == 7:
            logging.info("Выбран импорт из csv")
            model.import_list_csv()
            logging.info("Список сотрудников из csv импортирован")
            view.user_exit()

        else:
            print("Произошла неизвестная ошибка")

        logging.info("Действия успешно выполнены!")

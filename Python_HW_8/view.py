# def get_search_name() -> str:
#     return input("Введите фамилию для поиска: ")

# def print_table(data: list):
#     for el in data:
#         s = ''
#         for v, k in el.items():
#             s += f'{v}: {k}\n'
#         print(s)

def menu():
    print('Выберете действие:\n'
    '1. Показать всех учеников.\n'
    '2. Найти информацию ученика по фамилии.\n'
    '3. Показать учеников выбранного класса\n'
    '4. Добавить ученика. \n'
    '5. Изменить информацию ученика. \n'
    '6. Удалить ученика. \n'
    '7. Выйти.' )

    choice = int(input('Номер действия: '))
    return choice

def get_id() -> int:
    return int (input("Введите индетификатор ученика: "))

def get_surname() -> str:
    return input('Введите фамилию: ')

def get_first_name() -> str:
    return input('Введите имя: ')

def get_patronymic() -> str:
    return input('Введите отчество: ')

def get_class_number() -> str:
    return str (input("Введите номер класса: "))

def get_address() -> str:
    return input('Введите адрес: ')

def get_phone_number() -> int:
    return int(input('Введите номер телефона мамы/отца: '))

def get_phone_comment() -> str:
    return int(input('Введите чей номер телефона '))

def get_student() -> dict:
    r = {}
    r ["id"] = get_id()
    r ["surname"] = get_surname()
    r ["first_name"] = get_first_name()
    r ["patronymic_name"] = get_patronymic()
    r ["class_number"] = get_class_number()
    r ["address"] = get_address()
    r ["phone_number"] = get_phone_number()
    r ["phone_comment"] = get_phone_comment()
    return r

def get_changes() -> int:
    print("\nВыберите данные, которые необходимо поменять: ")
    print("1. id ")
    print("2. Фамилию ")
    print("3. Имя ")
    print("4. Отчество ")
    print("5. Номер класса ")
    print("6. Адрес ")
    print("7. Номер телефона родителя ")
    print("8. Изменить коментарий к номеру телефона ")
    return int(input("Введите нужный пункт: "))

def no_student_in_database():
    print("Такого студента нет в базе.")

def inf_by_surname(data: list, surname: str):
    for el in data:
        if el.get ('Фамилия') == surname:
            return f'{el.get ("Имя")}, {el.get ("Отчество")}, {el.get ("Номер класса")}, {el.get ("Адресс")}, {el.get ("Номер телефона мамы/папы")}, {el.get ("Комментарий")}'




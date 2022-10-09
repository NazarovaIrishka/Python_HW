def get_surname():
    surname = input('Введите фамилию: ')
    return surname

def get_first_name():
    first_name = input('Введите имя: ')
    return first_name

def get_patronymic():
    patronymic = input('Введите отчество: ')
    return patronymic

def get_phone_number():
    phone_number = input('Введите телефон: ')
    return phone_number

def get_address():
    address = input('Введите адрес: ')
    return address

def get_comment():
    comment = input('Введите комментарий: ')
    return comment

def search_by_surname(data: list, surname: str):
    for el in data:
        if el.get ('Фамилия') == surname:
            return el.get ('Телефон')
    
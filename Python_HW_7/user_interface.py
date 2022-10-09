import data_provider as prov
import logger as log

def surname_view():
    data = prov.get_surname()
    log.surname_logger(data)
    return data

def first_name_view():
    data = prov.get_first_name()
    log.first_name_logger(data)
    return data

def patronymic_view():
    data = prov.get_patronymic()
    log.patronymic_logger(data)
    return data

def phone_number_view():
    data = prov.get_phone_number()
    log.phone_number_logger(data)
    return data

def address_view():
    data = prov.get_address()
    log.address_logger(data)
    return data

def comment_view():
    data = prov.get_comment()
    log.comment_logger(data)
    return data

def menu():
    print('Выберете действие:\n'
    '1. Добавить абонента.\n'
    '2. Выйти.' )

    choice = int(input('Номер действия: '))
    return choice
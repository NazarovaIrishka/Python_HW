def surname_logger(d) -> str:
    with open ('tel.csv', 'a', encoding='utf-8') as file:
        file.write('{}   '
                    .format(d))

def first_name_logger(d) -> str:
    with open ('tel.csv', 'a', encoding='utf-8') as file:
        file.write('{}   '
                    .format(d))

def patronymic_logger(d) -> str:
    with open ('tel.csv', 'a', encoding='utf-8') as file:
        file.write('{}   '
                    .format(d))

def phone_number_logger(d):
    with open ('tel.csv', 'a') as file:
        file.write('{}   '
                    .format(d))
    
def address_logger(d) -> str:
    with open ('tel.csv', 'a', encoding='utf-8') as file:
        file.write('{}   ' 
                    .format(d))
    
def comment_logger(d) -> str:
    with open ('tel.csv', 'a', encoding='utf-8') as file:
        file.write('{}\n'
                    .format(d))
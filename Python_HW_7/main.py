import html_creater as hc
from data_provider import search_by_surname
from data_provider import get_surname
from user_interface import menu

choice = menu()

while (choice != 3):
    if choice == 1:
        print (hc.create())
    elif choice == 2:
        print('Работа завершена.\n')
        break
    choice = menu()

    
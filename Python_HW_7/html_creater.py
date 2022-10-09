from cgitb import html
from user_interface import surname_view
from user_interface import first_name_view
from user_interface import patronymic_view
from user_interface import phone_number_view
from user_interface import address_view
from user_interface import comment_view


def create ():
    style = 'style = "font-size: 24px;"'
    html = '<html>\n <head>\<head>\n <body>\n'
    html += '   <p {}> surname: {} c</p>\n'\
        .format(style, surname_view())
    html += '   <p {}> first_name: {} c</p>\n'\
        .format(style, first_name_view())
    html += '   <p {}> patronymic: {} c</p>\n'\
        .format(style, patronymic_view())
    html += '   <p {}> phone_number: {} c</p>\n'\
        .format(style, phone_number_view())
    html += '   <p {}> address: {} c</p>\n'\
        .format(style, address_view())
    html += '   <p {}> comment: {} c</p>\n'\
        .format(style, comment_view())
    html += '   </body>\n</html>'

    with open('book.html', 'w') as page:
        page.write(html)
    return html
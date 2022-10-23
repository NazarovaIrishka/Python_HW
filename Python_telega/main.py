import telebot

bot = telebot.TeleBot('5616370922:AAFdqmrwlkEkPXjAyc8ISp4TbN_PI01zFjo')

@bot.message_handler(commands = ['start'])

def start (message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

    bot.polling(none_stope=True)

@bot.message_handler()

def get_user_text(message):
    if message.text == "Helloo":
        bot.send_message(message.chat.id, "Привет!", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f'Твой id {message.from_user.id}', parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')

@bot.message_handler(commands = ['webside'])
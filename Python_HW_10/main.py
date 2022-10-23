import telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext 
from bot_commands import *

updater = Updater('5616370922:AAFdqmrwlkEkPXjAyc8ISp4TbN_PI01zFjo')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('menu', menu()))
updater.dispatcher.add_handler(CommandHandler('sum', sum))
updater.dispatcher.add_handler(CommandHandler('subtraction', sub))
updater.dispatcher.add_handler(CommandHandler('multiplication', mult()))
updater.dispatcher.add_handler(CommandHandler('dividing', div()))
updater.dispatcher.add_handler(CommandHandler('exponentiation', exponent()))


print ('Работа началась.')
updater.start_polling()
updater.idle()
import telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext 
import datetime

def log (update: Update, context: CallbackContext):
    mess_time = datetime.datetime.now()
    file = open('act.csv', 'a')
    file.write(f'{mess_time} {update.effective_user.first_name} : {update.message.text}\n ')
    file.close()
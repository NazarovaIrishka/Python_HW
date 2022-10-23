import telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext 
from logging import *

def hello (updater: Update, context: CallbackContext):
    log (updater, context)
    update.message.reply_text(f'Привет {update.effective_user.first_name} {update.effective_user.last_name}.\n Введи <b>/menu<b>, чтобы начать. ')

def menu (updater: Update, context: CallbackContext):
    log (updater, context)
    update.message.reply_text(f'/hello\n/menu\n/sum\n/sub\n/mult\n/div\n/exponent')

def sum (updater: Update, context: CallbackContext):
    log (updater, context)
    mess = update.message.tex
    items = mess.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')

def sub (updater: Update, context: CallbackContext):
    log (updater, context)
    mess = update.message.text
    items = mess.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} - {y} = {x - y}')

def mult (updater: Update, context: CallbackContext):
    log (updater, context)
    mess = update.message.text
    items = mess.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x}*{y} = {x * y}')

def div (updater: Update, context: CallbackContext):
    log (updater, context)
    mess = update.message.text
    items = mess.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x}/{y} = {x / y}')

def exponent (updater: Update, context: CallbackContext):
    log (updater, context)
    mess = update.message.text
    print ('Ведите число, которое нужно возвести в степень. Вторым числом введите саму степень.')
    items = mess.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x}**{y} = {x ** y}')
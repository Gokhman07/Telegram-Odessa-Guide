

# Импортируем необходимые компоненты
import logging
import os

from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.ext import Filters

from settings import TG_TOKEN
from handlers import *

from utility import get_keyboard

import sqlite3


PORT = int(os.environ.get('PORT', 5000))
updater=Updater(TG_TOKEN,use_context=True)
updater.start_webhook(listen="0.0.0.0",
port=int(PORT),
url_path=TG_TOKEN)
updater.bot.setWebhook('https://odessaguidebot2.herokuapp.com/' + TG_TOKEN)



logging.basicConfig(format='%(asctime)s-$(levelname)s-$(message)s',
                    level=logging.INFO,
                    filename='bot.log')


#нкцию main, которая соединяется с платформой Telegram
def main():

    # описываем функцию (тело функции)
    # создадим переменную my_bot, с помощью которой будем взаимодействовать с нашим ботом
    my_bot = Updater(TG_TOKEN, use_context=True)
    logging.info('Start bot')
   
    
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))  # обработчик команды start
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('🔙'),  main_keyboard))
   
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Клубы 🍹🍸|ТРЦ  🛍🛒|Отели  🏩🛎|Рестораны 🍷☕|Религиозные места ☮'), make_keyboard))
    
    
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Начать'), sms))  # обрабатываем текс кнопки
   
    my_bot.dispatcher.add_handler(MessageHandler(Filters.location, get_location))  # обработчик полученной геопозиции
    
    
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, sendPlace))

    
   # my_bot.dispatcher.add_handler(CallbackQueryHandler(inline_button_pressed))

  
    #my_mot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))  # обработчик текстового сообщения
    my_bot.start_polling()  # проверяет о наличии сообщений с платформы Telegram
    #my_bot.start_webhook(listen="0.0.0.0",

    #port=int(PORT),
   # url_path=TG_TOKEN)
    #my_bot.bot.setWebhook('https://mighty-savannah-13294.herokuapp.com/'+TG_TOKEN)

    my_bot.idle()  # бот будет работать пока его не остановят


if __name__ == "__main__":
    main()

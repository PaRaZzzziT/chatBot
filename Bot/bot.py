# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:58:30 2018

@author: Grani
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json

updater = Updater(token="699399793:AAECGDU5jxETG6dRkoy-yGJe7TJdIYnfPcY")
dispatcher = updater.dispatcher

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Heeey! Let's chat!")

def textMessage(bot, update):
    request = apiai.ApiAI("3117fc956ad245a086f328e9fb7328f2").text_request()
    request.lang = "en"
    request.session_id = "BernardettiBot"
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Sorry, I did not understand you(")
    
start_command_handler = CommandHandler("start", startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()

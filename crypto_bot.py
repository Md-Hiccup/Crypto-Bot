""" 
ref: https://dev.to/rizkyrajitha/get-notifications-with-telegram-bot-537l

Install library
    $ pip install python-dotenv
    $ pip install pyTelegramBotApi

Run the script
    $ python telegram-bot.py

To get chat-id
https://api.telegram.org/bot1<token>/sendMessage?chat_id=@channelName&text=123
"""
import telebot

from consts import *
import utils as utils

bot = telebot.TeleBot(API_KEY, parse_mode='MARKDOWN')


# To reply the particular message
@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hey! how's it going")

# To send the message
@bot.message_handler(commands=['hello', 'hi', 'Hello', 'Hi'])
def hello(message):
    bot.send_message(message.chat.id, "Hello")

# To send the message
@bot.message_handler(commands=['newCoin', 'newcoin'])
def new_coin(message):
    msg = utils.get_scrap_data(KEY_MESSAGE)
    bot.send_message(message.chat.id, msg)
    
    # Broadcast msg if new coin updated
    last_coin = utils.get_last_coin()
    if last_coin not in msg:
        utils.update_new_coin()

@bot.message_handler(commands=['help'])
def help(message):
    msg = f"""
    Welcome commands
    /hello - Hello
    /Greet - Hey! how's it going
    /newCoin - new coin update
    """
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
 

# utils.update_new_coin()

bot.polling()


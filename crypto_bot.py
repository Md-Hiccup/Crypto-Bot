""" 
Install library
    $ pip install python-dotenv
    $ pip install pyTelegramBotApi

Run the script
    $ python telegram-bot.py
"""
import os
from requests.api import request
import telebot
import requests

# Load .env file data
from dotenv import load_dotenv
import scrap_new_coin as scrappy

load_dotenv()

# Create telebot
API_KEY = os.getenv('API_KEY')
BOT_NAME = os.getenv('BOT_NAME')
CHAT_ID = os.getenv('CHAT_ID')

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
@bot.message_handler(commands=['newCoin'])
def new_coin(message):
    msg = scrappy.main()
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['help'])
def help(message):
    cmd_list = ['/Greet', '/hello', '/newCoin']
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
 
 
# BroadCast Message
def update_new_coin():
    import json
    msg = scrappy.main()
    
    # In url - sending message
    # url = f'https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHAT_ID}&text={msg}'
    # res = requests.get(url)

    # In Post method sending message
    url = 'https://api.telegram.org/bot{API_KEY}/sendMessage'
    data = {
        "chat_id" : CHAT_ID,
        "text" : msg,
        "parse_mode" : "markdown"
    }
    res = requests.post(url, json=data)


update_new_coin()

bot.polling()


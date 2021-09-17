""" 
Install library
    $ pip install python-dotenv
    $ pip install python-telegram-bot

Run the script
    $ python crypto_bot_new.py

To get chat-id
https://api.telegram.org/bot1<token>/sendMessage?chat_id=@channelName&text=123
"""
# Activate environment
HOME = '/Users/hussain/Projects/mystuff/'
activate_this = f"{HOME}/env/bin/activate_this.py" #for ubuntu
with open(activate_this) as f:
    code = compile(f.read(), activate_this, 'exec')
    exec(code, dict(__file__=activate_this))


from telegram.ext import Updater, CommandHandler,  MessageHandler, Filters

from consts import *
import utils as utils

def start(update, context):
    msg = "Welcome I Am The Binance New Coin Chat Bot! Will update you on latest binance coin"
    update.message.reply_text(msg)
    context.bot.sendMessage(chat_id=CHANNEL_NAME, text=msg)
    
def repeater(update, context):
    if utils.is_user_or_group(update):
        update.message.reply_text(update.message.text)
    elif utils.is_channel(update):
        context.bot.sendMessage(chat_id=CHANNEL_NAME, text=update.channel_post.text)

def help(update, context):
    msg = f"""
    Welcome commands
    /start - Welcome message
    /newCoin - new coin update
    """
    update.message.reply_text(msg, parse_mode='Markdown')

def new_coin(update, context):
    # Broadcast msg if new coin updated
    msg = utils.update_new_coin_by_bot()
    if msg:
        update.message.reply_text(msg, parse_mode='Markdown')
        context.bot.sendMessage(chat_id=CHANNEL_NAME, text=msg)
    else:
        msg = "No new coin updated on binance"
        update.message.reply_text(msg, parse_mode='Markdown')
    
def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('newCoin', new_coin))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(MessageHandler(Filters.text, repeater))
    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
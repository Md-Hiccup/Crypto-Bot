import os
# to load .env file data
from dotenv import load_dotenv

load_dotenv()

HOME = '/Users/hussain/Projects/mystuff/Crypto-Bot'

# import Environment Keys
API_KEY = os.getenv('API_KEY')
BOT_NAME = os.getenv('BOT_NAME')
CHAT_ID = os.getenv('CHAT_ID')
CHANNEL_NAME = os.getenv('CHANNEL_NAME')

KEY_MESSAGE = 'message'
KEY_COIN_LIST = 'coin_list'
KEY_ALL_DATA = 'all_data'

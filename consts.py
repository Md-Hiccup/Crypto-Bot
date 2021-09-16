import os
# to load .env file data
from dotenv import load_dotenv

load_dotenv()

# import Environment Keys
API_KEY = os.getenv('API_KEY')
BOT_NAME = os.getenv('BOT_NAME')
CHAT_ID = os.getenv('CHAT_ID')

KEY_MESSAGE = 'message'
KEY_COIN_LIST = 'coin_list'
KEY_ALL_DATA = 'all_data'

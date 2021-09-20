import os
# to load .env file data
from dotenv import load_dotenv
import pathlib

load_dotenv()

HOME = pathlib.Path(__file__).parent.absolute()

# import Environment Keys
API_KEY = os.getenv('API_KEY')
BOT_NAME = os.getenv('BOT_NAME')
CHAT_ID = os.getenv('CHAT_ID')
CHANNEL_NAME = os.getenv('CHANNEL_NAME')

KEY_MESSAGE = 'message'
KEY_COIN_LIST = 'coin_list'
KEY_ALL_DATA = 'all_data'

import requests

from consts import *
import scrap_new_coin as scrappy


# To get scrapping data of coin-market-cap
def get_scrap_data(data):
    message, coin_list = scrappy.main()
    if data == KEY_MESSAGE:
        return message
    elif data == KEY_COIN_LIST:
        return coin_list 
    elif data == KEY_ALL_DATA:
        return message, coin_list


# get last coin symbol from file
def get_last_coin():
    f = open('./new_coin.txt', 'r')
    last_coin = f.readline()
    f.close()
    return last_coin


# set last coin symbol to file
def set_last_coin(coin_symbol):
    f = open('./new_coin.txt', 'w')
    f.write(coin_symbol)
    f.close()


# Broadcase the new coin to channel
def update_new_coin():
    msg, coin_list = get_scrap_data(KEY_ALL_DATA)
    last_coin = get_last_coin()
    # print(coin_list[0])
    print(last_coin)
    
    if coin_list[0]['symbol'] != last_coin:
        set_last_coin(coin_list[0]['symbol'])

        # In json - sending message
        url = f'https://api.telegram.org/bot{API_KEY}/sendMessage'
        data = {
            "chat_id" : CHAT_ID,
            "text" : msg,
            "parse_mode" : "markdown"
        }
        res = requests.post(url, json=data)
        print(res.json())
    else:
        print('No new coin update')


# In url - sending message
# def send_message_url():
    # msg = 'Hello'
    # url = f'https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHAT_ID}&text={msg}'
    # res = requests.get(url)


"""
URL:    https://coinmarketcap.com/new/
Create Json file with new binance coin
Send New Coin message to telegram-bot
"""

from bs4 import BeautifulSoup
import requests
import json

url = 'https://coinmarketcap.com/new/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Get new coin data from coinmarketcap
def get_new_coin_data():
    tbody = soup.find('table', class_="h7vnx2-2 deceFm cmc-table").find('tbody')
    # print(len(tbody))

    pre_link = 'https://coinmarketcap.com'
    new_coins = []

    for row in tbody:
        row_td = row.find_all('td')
        coin = {}
        
        # Check Binance only
        coin_platform = row.find('div', class_='s8fs2i-2 TBaWj').get_text()
        coin['platform'] = coin_platform
        
        if coin_platform != "Binance Coin":
            continue

        # Get Coin Name
        coin_name = row.find('p', class_="sc-1eb5slv-0 iworPT").get_text()
        coin['name'] = coin_name
        
        # Get Coin Symbol
        coin_symbol = row.find('p', class_="sc-1eb5slv-0 gGIpIK coin-item-symbol").get_text()
        coin['symbol'] = coin_symbol
        
        # Get Coin link
        coin_link = row.find('a', class_='cmc-link').get('href')
        coin['link'] = pre_link + coin_link
        
        # Get Coin Price
        coin_price = row_td[3].get_text()
        coin['price'] = coin_price
        
        # Get 1hr update
        coin_one = row.find('span', class_='sc-15yy2pl-0 hzgCfk')
        coin_one_update = None
        if coin_one: 
            coin_one_update = '+' + coin_one.get_text()
            if 'down' in coin_one.find('span').attrs['class'][0]:
                coin_one_update = '-' + coin_one.get_text()
        coin['1hr'] = coin_one_update
        
        # Get 24hr update
        coin_twentyfour = row.find('span', class_='sc-15yy2pl-0 kAXKAX')
        coin_twentyfour_update = None
        if coin_twentyfour:
            coin_twentyfour_update = '+' + coin_twentyfour.get_text()
            if 'down' in coin_twentyfour.find('span').attrs['class'][0]:
                coin_twentyfour_update = '-' + coin_twentyfour.get_text()
        coin['24hr'] = coin_twentyfour_update

        # Get Volume
        coin_volume = row_td[-4].get_text()
        coin['volume'] = coin_volume
                
        # Get Coin time
        updated = row_td[-2].get_text()
        coin['time'] = updated
        
        new_coins.append(coin)
        # break
    return new_coins

# Format coin data for sending message in channel
def format_coin_list(last_coin):
    lc_name = last_coin.get('name')
    lc_symbol = last_coin.get('symbol')
    lc_price = last_coin.get('price')
    lc_time = last_coin.get('time')
    lc_link = last_coin.get('link')
    # msg = f'{"Hi": <16} StackOverflow!'
    space = 15
    msg = f'{"Name": <{space}} {lc_name}\n'
    msg += f'{"Symbol": <{space}} [{lc_symbol}]({lc_link})\n'
    msg += f'{"Price": <{space}} {lc_price}\n'
    msg += f'{"Time": <{space}} {lc_time}'
    return msg

# main function
def main():
    new_coin_list = get_new_coin_data()
    if not new_coin_list:
        # print('Not Found')
        return "Not Found"
        
    new_coin_message = format_coin_list(new_coin_list[0])
    # print(new_coin_message)
    
    # print(json.dumps(new_coin_list, indent=4))
    # print(len(new_coins))
    
    return new_coin_message


# For Testing purpose: uncomment below line
# main()


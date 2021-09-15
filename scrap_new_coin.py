"""
URL:    https://coinmarketcap.com/new/

Create Json file with new binance coin

"""
from bs4 import BeautifulSoup
import requests
import json

url = 'https://coinmarketcap.com/new/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

tbody = soup.find('table', class_="h7vnx2-2 deceFm cmc-table").find('tbody')
print(len(tbody))

link_pre = 'https://coinmarketcap.com'
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
    coin['link'] = link_pre + coin_link
    
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
    
    # print(row.prettify())
    new_coins.append(coin)
    # break

print(json.dumps(new_coins, indent=4))
# print(len(new_coins))
import os

import requests

apikey = os.environ.get('RAPIDAPIKEY')
url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={apikey}'
r = requests.get(url)
response = r.json()

data = response['Realtime Currency Exchange Rate']

btc = {
    'from_currency_code': data['1. From_Currency Code'],
    'from_currency_name': data['2. From_Currency Name'],
    'to_currency_code': data['3. To_Currency Code'],
    'to_currency_name': data['4. To_Currency Name'],
    'exchange_rate': data['5. Exchange Rate'],
    'last_refreshed': data['6. Last Refreshed'],
    'time_zone': data['7. Time Zone'],
    'bid_price': data['8. Bid Price'],
    'ask_price': data['9. Ask Price']
}
print(btc)
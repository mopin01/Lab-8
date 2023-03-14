import requests

def get_exchange_rate():
    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(coindesk_url)
    data = response.json()
    return data['bpi']['USD']['rate_float']

def bitcoin_to_usd(bitcoin):
    bitcoin_value_in_dollars = bitcoin * get_exchange_rate()
    return bitcoin_value_in_dollars
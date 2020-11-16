import alpaca_trade_api as tradeapi
from api import *
# Fetch Data
# Sort Data based on parameters (Parameters are: timeframe, price, volume)
# Execute trade on one stock that comes closest to parameters
# Make sure position is held for at least 24 hours
#

endpoint = 'https://paper-api.alpaca.markets'

api_key = get_api_key()
secret_api_key = get_api_secret()

api = tradeapi.REST('<key_id>', '<secret_key>', base_url='https://paper-api.alpaca.markets')
user_stock = input("What stock would you like to search?")
stock = api.get_position(user_stock)
print(stock)

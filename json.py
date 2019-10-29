#Modules required to perform functions
import requests
import json
import math
import datetime

#Using the bitcoin API to get the value of bitcoins today and yesterday
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
package_json = r.json()

#Creating date variables for my comparisons function
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)

#Parsing date from the JSON so that i only recieve the rate from dictionary
bitcoin_price_usd = package_json['bpi']['USD']['rate']
bitcoin_price_gbp = package_json['bpi']['GBP']['rate']
bitcoin_price_eur = package_json['bpi']['EUR']['rate']

all_prices = bitcoin_price_eur, bitcoin_price_gbp, bitcoin_price_usd

#Getting the rate of bitcoin today
bitcoin_today_usd = bitcoin_price_usd, today
bitcoin_today_gbp = bitcoin_price_gbp, today
bitcoin_today_eur = bitcoin_price_eur, today

bitcoin_today = bitcoin_today_usd, bitcoin_today_gbp, bitcoin_today_eur

#Getting the rate of bitcoin yesterday
bitcoin_yesterday_usd = bitcoin_price_usd, yesterday
bitcoin_yesterday_gbp = bitcoin_price_gbp, yesterday
bitcoin_yesterday_eur = bitcoin_price_eur, yesterday

bitcoin_yesterday = bitcoin_yesterday_usd, bitcoin_yesterday_gbp, bitcoin_yesterday_eur

#printing out variable to check code runs as expected.

print(bitcoin_yesterday)
"""
#caparing prices
if bitcoin_today > bitcoin_yesterday:
    print('it is more')
else:
    print('it didnt work')
"""

#for x in bitcoin_yesterday:
    #print (x)


#packages_str = json.dumps(package_json, indent=2)
#print(bitcoin_today_usd, bitcoin_price_eur, bitcoin_price_gbp)
#def bitcoin_price_test():


#for x in all_prices:
#    print (x)

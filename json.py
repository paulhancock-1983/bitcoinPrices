import requests
import json
import math
import datetime


r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
package_json = r.json()

bitcoin_price_usd = package_json['bpi']['USD']['rate']
bitcoin_price_gbp = package_json['bpi']['GBP']['rate']
bitcoin_price_eur = package_json['bpi']['EUR']['rate']

all_prices = bitcoin_price_eur, bitcoin_price_gbp, bitcoin_price_usd

#packages_str = json.dumps(package_json, indent=2)

bitcoin_today_usd = bitcoin_price_usd, datetime.datetime.now()
bitcoin_today_gbp = bitcoin_price_gbp, datetime.datetime.now()
bitcoin_today_eur = bitcoin_price_eur, datetime.datetime.now()

bitcoin_today = bitcoin_today_usd, bitcoin_today_gbp, bitcoin_today_eur

for x in bitcoin_today:
    print (x)
#print(bitcoin_today_usd, bitcoin_price_eur, bitcoin_price_gbp)
#def bitcoin_price_test():


#for x in all_prices:
#    print (x)

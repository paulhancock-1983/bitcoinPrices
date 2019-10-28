import requests
import json


r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
package_json = r.json()

bitcoin_price_usd = package_json['bpi']['USD']['rate']
bitcoin_price_gbp = package_json['bpi']['GBP']['rate']
bitcoin_price_eur = package_json['bpi']['EUR']['rate']

all_prices = bitcoin_price_eur, bitcoin_price_gbp, bitcoin_price_usd

#packages_str = json.dumps(package_json, indent=2)

print (all_prices)

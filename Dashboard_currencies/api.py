from datetime import date, timedelta
from pprint import pprint

import requests


def get_rates(currencies, days=30):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)
    list_currencies = ",".join(currencies)
    url = "https://www.docstring.fr/api/rates/history/"
    
    #https://www.docstring.fr/api/rates/history/?start_at=2020-01-01&end_at=2020-01-04&symbols=USD,CAD
    url_query = f'{url}?start_at={start_date}&end_at={end_date}&symbols={list_currencies}'
    requete = requests.get(url_query)
    
    if not requete and not requete.json():
        return False, False
    
    api_rates = requete.json().get("rates")
    
    all_rates = {currency:[] for currency in currencies}
    all_days = api_rates.keys()
    
    for each_day in all_days:
        for currency, rate in api_rates[each_day].items():
            all_rates[currency].append(rate)
    
    return all_days, all_rates
        
    

list_currencies = ["USD", "EUR"]
get_rates(list_currencies)
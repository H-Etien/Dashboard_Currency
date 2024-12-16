from datetime import date, timedelta

import requests


def get_rates(currencies: list[str], days:int = 30):
    """Avoir le taux de chaque monnaie à un intervalle de jour

    Args:
        currencies (list): liste des monnaies
        days (int, optional): l'intervalle de jour. Defaults to 30.

    Returns:
        dict:   retourne 2 dict
                all_days = liste de jour
                all_rates = dict avec key: monnaie et valeur: liste du taux
    """
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
    all_days = list(api_rates.keys())
    
    for each_day in all_days:
        for currency, rate in api_rates[each_day].items():
            all_rates[currency].append(rate)
    
    return all_days, all_rates
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

import api

# Create your views here.

list_currencies = ["USD", "EUR"]

def dashboard(request):
    
    return render(
        request,
        'devise/index.html',
        context={
            "data": list_currencies,
        }
    )

#crée une page avec une API pour que le fichier index.js puisse récupérer les valeurs
@api_view(["GET"])
def get_currency_data(request, days_range):
    if not days_range:
        days_range = 7
        
    days, rates = api.get_rates(currencies=list_currencies, days=days_range)
    dict_currency = {
        "days" : days,
        "rates" : rates,
    }
    return Response(dict_currency)
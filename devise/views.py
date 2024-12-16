from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

import api

# Create your views here.
def dashboard(request):
    return render(
        request,
        'devise/index.html'
    )

#crée une page avec une API pour que le fichier index.js puisse récupérer les valeurs
@api_view(["GET"])
def get_currency_data(request):
    days, rates = api.get_rates(currencies=["USD", "EUR", "CNY"], days=20)
    dict_currency = {
        "days" : days,
        "rates" : rates,
    }
    return Response(dict_currency)
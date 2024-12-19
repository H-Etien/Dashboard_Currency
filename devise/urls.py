from django.urls import path
from .views import dashboard, get_currency_data

urlpatterns = [
    path('', dashboard, name="home"),
    path('api/', get_currency_data, name="api_currency")
]

from django.urls import path
from .views import dashboard, get_currency_data

urlpatterns = [
    path('', dashboard, name="home"),
    path('api/days=<int:days_range>', get_currency_data, name="api_currency")
]

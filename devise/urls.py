from django.urls import path
from .views import dashboard, get_currency_data

urlpatterns = [
    path('', dashboard),
    path('api/', get_currency_data)
]


from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path('search/', views.search_flights, name='search_flights'),
]
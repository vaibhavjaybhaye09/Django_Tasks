from django.urls import path
from .views import *

urlpatterns =[
    path('', home , name='home'),
    path('available/',view_available_cars, name='view_available_cars'),
    path('rent', rent_car, name='rent_car'),
    path('rented',view_rented_cars, name='view_rented_cars'),
    path('return/',return_car, name='return_car'),
    path('history/', view_rental_history, name= 'view_rental_history'),
]
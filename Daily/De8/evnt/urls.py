from .views import *
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('create/', e_create, name='e_create'),
    path('update/<int:pk>/',e_update, name='e_update'),
    path('delete/<int:pk>/',e_delete, name='e_update'),
       
]

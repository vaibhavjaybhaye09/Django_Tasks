from django.urls import path
from .views import *

urlpatterns = [
    path('',gall_l, name='gall_l'),
    path('create/', gall_c , name='gall_c'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
]

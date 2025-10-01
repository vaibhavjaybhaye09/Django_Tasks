from django.urls import path
from .views import *

urlpatterns = [
   path('', profile_list, name='profule_list'),
   path('create/', ac_create, name='ac_create'),
   path('profile/<int:pk>/', profile, name='profile'),
   path('update/<int:pk>/', ac_update, name='ac_update'),
   path('delete/<int:pk>/', ac_delete, name='ac_delete'),
   path('list/<int:pk>/', profile_list, name='profule_list'),

]
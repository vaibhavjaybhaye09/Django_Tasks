from django.urls import path
from .views import *

urlpatterns = [
   path('', emp_list , name='emp_list'),
   path('create/', emp_form, name='emp_form'),
   path('update/<int:id>/', emp_update, name='emp_update'),
   path('delete/<int:id>/', emp_del, name='emp_del'),
   path('position/create/', position_form, name='position_form'),
   path('position/update/<int:id>/', position_update, name='position_update'),
   path('position/delete/<int:id>/', position_delete, name='position_delete'),
]

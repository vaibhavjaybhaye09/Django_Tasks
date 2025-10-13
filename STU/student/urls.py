from django.urls import path
from .views import *

urlpatterns = [
    path('', stu_list,name='stu_list'),
    path('create/',stu_create,name='stu_create'),
    path('update/<int:pk>/', stu_update, name='stu_update'),
    path('delete/<int:pk>/', Stu_del, name='Stu_del'),

]
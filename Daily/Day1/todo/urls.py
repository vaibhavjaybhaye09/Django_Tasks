from django.conf import settings
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path('', todo_list, name= 'todo_list'),
path('create/', todo_create, name= 'todo_create'),
path('update/<int:pk>/', todo_update, name= 'todo_update'),
path('delete/<int:pk>/', todo_delete, name= 'todo_delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
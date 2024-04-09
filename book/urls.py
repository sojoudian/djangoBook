from django.urls import path
from .views import book_list
from . import views

urlpattern = [
    path('book/', book_list, name='book_list'),
]
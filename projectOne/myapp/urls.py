from django.urls import path
from . import views

urlpatterns = [
    path('myapp/', views.hello_world, name='hello_world'),
]

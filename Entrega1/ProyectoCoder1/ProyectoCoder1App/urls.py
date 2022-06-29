
from django.urls import path

from ProyectoCoder1App import views


urlpatterns = [
    
    path("", views.index),
    path("jovenes", views.jovenes),
    path("adultos", views.adultos),
    path("viejos", views.viejos),
    
]

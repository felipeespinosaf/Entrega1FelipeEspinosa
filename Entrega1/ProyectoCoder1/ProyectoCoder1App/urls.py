
from django.urls import path

from ProyectoCoder1App import views


urlpatterns = [
    
    path("", views.index,name="inicio"),
    path("jovenes", views.jovenes,name="jovenes"),
    path("adultos", views.adultos,name="adultos"),
    path("viejos", views.viejos,name="viejos"),
    
]

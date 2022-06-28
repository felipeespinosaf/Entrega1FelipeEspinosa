from django.urls import path
from ProyectoCoder1App import views


urlpatterns = [
    
    path('', views.index),
    
    path('', views.jovenes),
    
    path('', views.adultos),
    
    path('', views.viejos),
    
]

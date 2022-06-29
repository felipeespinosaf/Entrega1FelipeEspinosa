
from django.urls import path

from ProyectoCoder1App import views


urlpatterns = [
    
    path("", views.index,name="inicio"),
    path("jovenes", views.jovenes,name="jovenes"),
    path("adultos", views.adultos,name="adultos"),
    path("viejos", views.viejos,name="viejos"),
    path("crear_joven",views.crear_joven,name="crear_joven"),
    path("crear_adulto",views.crear_adulto,name="crear_adulto"),
    path("crear_viejo",views.crear_viejo,name="crear_viejo"),
    path("buscar_nombre_joven",views.buscar_nombre_joven,name="buscar_nombre_joven"),
    path("buscar_nombre_adulto",views.buscar_nombre_adulto,name="buscar_nombre_adulto"),
    path("buscar_nombre_viejo",views.buscar_nombre_viejo,name="buscar_nombre_viejo"),
    # path("joven_formulario", views.joven_formulario, name="joven_formulario"),
    
]

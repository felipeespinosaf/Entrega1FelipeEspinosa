from django.http import HttpResponse
from django.shortcuts import render

from ProyectoCoder1App import forms
from .models import*
# from ProyectoCoder1App import JovenFormulario
# Create your views here.


def index(request):
    
    return render(request,"ProyectoCoder1App/index.html")
    # return HttpResponse ("Vista de index")

# def jovenes(request):
    
#     return render(request,"ProyectoCoder1App/jovenes.html")
#     # return HttpResponse ("Vista de jovenes")

def jovenes(request):
    
    jovenes=Joven
    
    lista_jovenes = Joven.objects.all()
    
    return render(request, "ProyectoCoder1App/jovenes.html", {"jovenes":lista_jovenes})

def crear_joven(request):
    
    return render(request, "ProyectoCoder1App/formulario_joven.html",{})

def adultos(request):
    
    adultos=Adulto
    
    lista_adultos = Adulto.objects.all()
    
    return render(request, "ProyectoCoder1App/adultos.html", {"adultos":lista_adultos})
    # return HttpResponse ("Vista de adultos")

def viejos(request):
    
    viejos=Viejo
    lista_viejos = Viejo.objects.all()
    
    return render(request, "ProyectoCoder1App/viejos.html", {"viejos":lista_viejos})
    # return HttpResponse ("Vista de viejos")
    
# def joven_formulario(request):
    
    
#     if request.method =="Post":
        
#         miFormulario=JovenFormulario(request.POST)
        
#         print(miFormulario)
        
#         if miFormulario.is_valid:
            
#             informacion = miFormulario.cleaned_data
            
        
#             joven=Joven(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'])
            
#             joven.save()
        
#             return render(request, "ProyectoCoder1App/index.html")
#     else:
#         miFormulario=JovenFormulario()
    
    
#     return render(request, "ProyectoCoder1App/joven_formulario.html", {"miFormulario": miFormulario})
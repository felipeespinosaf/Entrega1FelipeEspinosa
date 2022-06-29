from django.http import HttpResponse
from django.shortcuts import redirect, render

from ProyectoCoder1App import forms
from .models import*


from .forms import *
# from ProyectoCoder1App import J
# ovenFormulario
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
    
    
    if request.method =="POST":
        
        formulario=NuevoJoven(request.POST)
        
        if formulario.is_valid():
            
            info_joven= formulario.cleaned_data
        
            joven=Joven(nombre=info_joven["nombre"], apellido=info_joven["apellido"], edad=int(info_joven["edad"]))
            
            joven.save()
            
            return redirect("jovenes")
        
        else:
            return render(request,"ProyectoCoder1App/formulario_joven.html",{"form":formulario})
    else:
        
        formulario_vacio = NuevoJoven()
        
        return render(request,"ProyectoCoder1App/formulario_joven.html",{"form":formulario_vacio})
    
    

def adultos(request):
    
    adultos=Adulto
    
    lista_adultos = Adulto.objects.all()
    
    return render(request, "ProyectoCoder1App/adultos.html", {"adultos":lista_adultos})
    # return HttpResponse ("Vista de adultos")
    
def crear_adulto(request):
    
    
    if request.method =="POST":
        
        formulario=NuevoAdulto(request.POST)
        
        if formulario.is_valid():
            
            info_adulto= formulario.cleaned_data
        
            adulto=Adulto(nombre=info_adulto["nombre"], apellido=info_adulto["apellido"], edad=int(info_adulto["edad"]))
            
            adulto.save()
            
            return redirect("adultos")
        
        else:
            return render(request,"ProyectoCoder1App/formulario_adulto.html",{"form":formulario})
    else:
        
        formulario_vacio = NuevoAdulto()
        
        return render(request,"ProyectoCoder1App/formulario_adulto.html",{"form":formulario_vacio})

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
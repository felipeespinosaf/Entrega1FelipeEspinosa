from django.http import HttpResponse
from django.shortcuts import render

from Entrega1.ProyectoCoder1.ProyectoCoder1App.forms import JovenFormulario
from .models import*
from ProyectoCoder1App import JovenFormulario
# Create your views here.


def index(request):
    
    return render(request,"ProyectoCoder1App/index.html")
    # return HttpResponse ("Vista de index")

def jovenes(request):
    
    return render(request,"ProyectoCoder1App/jovenes.html")
    # return HttpResponse ("Vista de jovenes")

def adultos(request):
    
    return render(request,"ProyectoCoder1App/adultos.html")
    # return HttpResponse ("Vista de adultos")

def viejos(request):
    
    return render(request,"ProyectoCoder1App/viejos.html")
    # return HttpResponse ("Vista de viejos")
    
def joven_formulario(request):
    
    
    if request.method =="Post":
        
        miFormulario=JovenFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
        
            joven=Joven(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'])
            
            joven.save()
        
            return render(request, "ProyectoCoder1App/index.html")
    else:
        miFormulario=JovenFormulario()
    
    
    return render(request, "ProyectoCoder1App/joven_formulario.html", {"miFormulario": miFormulario})
from django.http import HttpResponse
from django.shortcuts import render

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
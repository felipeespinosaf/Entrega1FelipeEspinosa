from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("vista index")
    # return render(request, "",{})

def jovenes(request):
    return HttpResponse("Vista jovenes")
    # return render(request, ""{})

def adultos(request):
    return HttpResponse("Vista adultos")
    # return render(request, ""{})

def viejos(request):
    return HttpResponse("Vista viejos")

    
    # return render(request, ""{})
from django.db import models
from django.forms import IntegerField

# Create your models here.

class Joven(models.Model):
    
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.IntegerField()
    
class Adulto(models.Model):
    
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.IntegerField()
    
class Viejo(models.Model):
    
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.IntegerField()
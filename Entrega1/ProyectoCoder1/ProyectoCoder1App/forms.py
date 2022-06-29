from django import forms


class NuevoJoven(forms.Form):
    
    nombre= forms.CharField(max_length=30,label="Nombre")
    
    apellido= forms.CharField(max_length=30,label="Apellido")
    
    edad= forms.IntegerField(min_value=0,label="Edad")
    
class NuevoAdulto(forms.Form):
    
    nombre= forms.CharField(max_length=30,label="Nombre")
    
    apellido= forms.CharField(max_length=30,label="Apellido")
    
    edad= forms.IntegerField(min_value=0,label="Edad")
    
class NuevoViejo(forms.Form):
    
    nombre= forms.CharField(max_length=30,label="Nombre")
    
    apellido= forms.CharField(max_length=30,label="Apellido")
    
    edad= forms.IntegerField(min_value=0,label="Edad")
from django import forms


class JovenFormulario(forms.Form):
    
    nombre= forms.CharField()
    
    apellido= forms.CharField()
    
    edad= forms.IntegerField()
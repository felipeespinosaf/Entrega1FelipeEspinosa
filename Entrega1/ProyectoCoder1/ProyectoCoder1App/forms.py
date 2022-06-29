from django import forms


class NuevoJoven(forms.Form):
    
    nombre= forms.CharField(max_length=30)
    
    apellido= forms.CharField(max_length=30)
    
    edad= forms.IntegerField(min_value=0)
    
# class AdultoFormulario(forms.Form):
    
#     nombre= forms.CharField()
    
#     apellido= forms.CharField()
    
#     edad= forms.IntegerField()
    
# class ViejoFormulario(forms.Form):
    
#     nombre= forms.CharField()
    
#     apellido= forms.CharField()
    
#     edad= forms.IntegerField()
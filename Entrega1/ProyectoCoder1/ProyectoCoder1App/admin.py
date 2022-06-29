from django.contrib import admin

# Register your models here.


from ProyectoCoder1App.models import *


class JovenAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'apellido', 'edad')
    search_fields= ('nombre', 'apellido', 'edad')
    
    
class AdultoAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'apellido', 'edad')
    search_fields= ('nombre', 'apellido', 'edad')
    
    
class ViejoAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'apellido', 'edad')
    search_fields= ('nombre', 'apellido', 'edad')



admin.site.register(Joven,JovenAdmin)
admin.site.register(Adulto,AdultoAdmin)
admin.site.register(Viejo,ViejoAdmin)

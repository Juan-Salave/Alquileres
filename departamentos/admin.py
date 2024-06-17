from django.contrib import admin
from .models import Barrio, Departamento, ImagenDepartamentos, Moneda

class ImagenDepartamentosAdmmin(admin.TabularInline):           # Clase para incluir img en linea 1 + 1 + 1 
    model = ImagenDepartamentos
    
class DepartamentosAdmin(admin.ModelAdmin):
    list_display = ['clave','barrio','moneda','precio']               # Campos visibles en el admin
    list_editable = ['precio','moneda']                                        # Campos editables    
    search_fields =['clave']                                          # Campo de busqueda
    list_filter = ['barrio','precio']                                 # Campo de filtrado / Barra lateral
    list_per_page = 7
    inlines = [                                                       # Incluimos la Class de imagenes
        ImagenDepartamentosAdmmin
    ]

admin.site.register(Barrio)
admin.site.register(Moneda)
admin.site.register(Departamento, DepartamentosAdmin)           # Visibles en el Admin
admin.site.register(ImagenDepartamentos)

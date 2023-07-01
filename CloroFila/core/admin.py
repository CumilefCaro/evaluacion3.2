from django.contrib import admin
from.models import Categoria, producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','descripcion','exterior','categoria','fecha_germinacion','stock']
    list_editable= ['precio','exterior','categoria','fecha_germinacion','stock']
    
    


# Register your models here.
admin.site.register(Categoria)
admin.site.register(producto, ProductoAdmin)




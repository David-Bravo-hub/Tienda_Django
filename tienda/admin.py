from django.contrib import admin
from .models import Producto 

class ProductoAdmin(admin.ModelAdmin):
    # Columnas que se mostrarán en la tabla de administración
    list_display = ('id', 'nombre', 'precio', 'stock')
    
    # Agregar una barra de búsqueda por nombre del producto
    search_fields = ('nombre',)
    
    # Filtros laterales por precio o stock (puedes ajustarlo según tus campos)
    list_filter = ('precio',)

# Registramos el modelo junto con su configuración personalizada
admin.site.register(Producto, ProductoAdmin)
from django.contrib import admin
from .models import Producto

#admin.site.register(Producto)
@admin.register(Producto)
class AdminProducto(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'descripcion', 'precio', 'formadepago')
    list_filter = ('nombre', 'categoria')
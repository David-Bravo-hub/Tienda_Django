from django.shortcuts import render, get_object_or_404
from .models import Producto

def inicio(request):
    # Muestra la lista de todos los productos en la página principal
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render(request, 'tienda/index.html', contexto)

def detalle_producto(request, producto_id):
    # Muestra el detalle de un producto específico según su ID
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'tienda/detalle.html', {'producto': producto})

def nosotros(request):
    # Muestra la página de información del taller o tienda
    return render(request, 'tienda/nosotros.html')

def contacto(request):
    # Muestra la página de contacto
    return render(request, 'tienda/contacto.html')
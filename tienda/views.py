from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import ProductoSerializer

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

# --- OPERACIONES CRUD PROTEGIDAS PARA LA EVALUACIÓN 2 ---

@login_required
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        descripcion = request.POST.get('descripcion')
        
        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            stock=stock,
            descripcion=descripcion
        )
        return redirect('inicio')
    return render(request, 'tienda/crear_producto.html')

@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.descripcion = request.POST.get('descripcion')
        producto.save()
        return redirect('inicio')
    return render(request, 'tienda/editar_producto.html', {'producto': producto})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    producto.delete()
    return redirect('inicio')

# --- VISTA PARA LA API RESTful (UNIDAD 3) ---

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
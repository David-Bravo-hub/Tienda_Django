from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router automático para la API RESTful
router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet)

urlpatterns = [
    # Tus rutas web anteriores (no las borres)
    path('', views.inicio, name='inicio'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('producto/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    
    # Endpoints de la API RESTful (JSON)
    path('api/', include(router.urls)),
]
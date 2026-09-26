from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    
    # --- RUTAS CRUD PARA LA EVALUACIÓN 2 ---
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('producto/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]
from django.urls import path 
from .views import *

urlpatterns = [
    path('', index_view, name='index_view' ),
    path('about/', about_view, name='about_view' ),

    path('listar_producto/', listar_producto_view, name='listar_producto' ),
    path('agregar_producto/', agregar_producto_view, name='agregar_producto' ),
    path('ver_producto/<int:id_prod>/', ver_producto_view, name='ver_producto' ),
    path('editar_producto/<int:id_prod>/', editar_producto_view, name='editar_producto' ),
    path('eliminar_producto/<int:id_prod>/', eliminar_producto_view, name='eliminar_producto' ),

    path('registrarse/', registrarse_view, name='registrarse' ),
]
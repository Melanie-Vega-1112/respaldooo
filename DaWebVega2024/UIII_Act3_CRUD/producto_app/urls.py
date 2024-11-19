from django.urls import path 
from producto_app import views

urlpatterns = [
    path("", views.inicio_vista,name="inicio_vista"),
    path("registrarProducto/" ,views.registrarProducto,name="registrarProducto")
]
from .models import Producto
from django.shortcuts import render, redirect
from django.http import HttpResponse

def inicio_vistaProductos(request):
    losproductos = Producto.objects.all()
    return render(request, "registrarProductos.html", {"misproductos": losproductos})

def registrarProducto(request):
    nombre=request.POST["txtnombre"]
    idproducto=request.POST["txtid"]
    Descripcion=request.POST["txtdesc"]
    Precio=request.POST["txtprecio"]
    Categoria=request.POST["txtcat"]
    Material=request.POST["txtmat"]
    stock=request.POST["txtstock"]

    guardarproducto=Producto.objects.create(nombre=nombre, idproducto=idproducto, Descripcion=Descripcion, Precio=Precio, Categoria=Categoria, Material=Material, stock=stock)

    return redirect("/")
def eliminarProducto(request, idproducto):
    if request.method == 'POST':
        # Buscar el producto por ID y eliminarlo
        producto = Producto.objects.get(idproducto=idproducto)
        producto.delete()
    # Redirigir de vuelta a la lista de productos después de eliminar
    return redirect('registrarProductos') 

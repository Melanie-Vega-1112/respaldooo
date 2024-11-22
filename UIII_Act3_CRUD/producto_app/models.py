from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    idproducto = models.PositiveSmallIntegerField(primary_key=True)  # Solo este campo debe ser la clave primaria
    Descripcion = models.CharField(max_length=100)
    Precio = models.PositiveSmallIntegerField()  # Se eliminó primary_key=True aquí
    Categoria = models.CharField(max_length=100)
    Material = models.CharField(max_length=100)
    stock = models.PositiveSmallIntegerField()  # Se eliminó primary_key=True aquí

    def __str__(self):
        return self.nombre

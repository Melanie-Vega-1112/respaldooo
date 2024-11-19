from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=100)
    idproducto=models.PositiveSmallIntegerField(primary_key=True)
    def __str__ (self):
        return self.nombre

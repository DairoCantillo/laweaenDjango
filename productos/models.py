from __future__ import unicode_literals
from django.db import models



class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)
    categoria = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    formadepago = models.CharField(max_length=30)
    imagen = models.ImageField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id',)
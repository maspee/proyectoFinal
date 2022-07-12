from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    rut = models.CharField(max_length=12, verbose_name='Rut')
    edad = models.IntegerField(verbose_name='Edad')
    correo = models.CharField(max_length=50, verbose_name='Email')
    direccion = models.CharField(max_length=50, verbose_name='Dirección')
    telefono = models.IntegerField(verbose_name='Teléfono')
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Receta')
    descripcion = models.TextField(verbose_name='Descripción', null=True) 
    autor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Descripción: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parents= False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete() 
    
   
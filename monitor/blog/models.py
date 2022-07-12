from django.conf import settings
from django.db import models
from django.utils import timezone

class Publicacion(models.Model): #Post
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now) #created_date
    fecha_publicacion = models.DateTimeField(blank=True, null=True) #published_date

    def publicacion(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo


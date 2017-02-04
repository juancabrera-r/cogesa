from django.db import models

# Create your models here.

#HOME -> Página principal, es donde se representa las "mejores" imagenes.
#Trabajos -> Página donde se representan la foto princpal de cada trabajo.
#Album -> Contiene todas las fotos de cada trabajo

# Controla la visibilidad de las fotos en HOME, TRABAJOS y ALBUM



class Photo(models.Model):

    name = models.CharField(max_length=150)  # Nombre de la fotografía
    url = models.URLField()
    description = models.TextField(null=True, blank=True)  # Descripción de la fotografía
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    modified_at = models.DateTimeField(auto_now=True)  # Fecha de modificación

    def __str__(self):
        return self.name

from django.db import models
from django.db.models.fields import CharField, URLField, DateField
from django.db.models.fields.files import ImageField


# Create your models here.
class Proyectos(models.Model):
    titulo = CharField(max_length=100)
    descripcion = CharField(max_length=300)
    imagen = ImageField("portafolio/imagenes")
    url = URLField(blank=True)
    ultima_actualizacion = DateField(auto_now=True)

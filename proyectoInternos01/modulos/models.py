from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Modulo(models.Model):
    nombre = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 100)
    img = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.nombre
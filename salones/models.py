from django.db import models

class Salon(models.Model):
    nombre = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return "Salon " + self.nombre

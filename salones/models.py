from django.db import models

class Salon(models.Model):
    nombre = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre

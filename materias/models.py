from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    semestre = models.PositiveIntegerField(default =1,validators = [MinValueValidator(1),MaxValueValidator(10)])

    def __str__(self):
        return self.nombre
    

from django.db import models

from salones.models import Salon
from materias.models import Materia
from alumnos.models import Alumno

class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    HORARIOS = [
    ('7-8', '7-8'),
    ('8-9', '8-9'),
    ('9-10', '9-10'),
    ('10-11', '10-11'),
    ('11-12', '11-12'),
    ('12-1', '12-1'),
    ] 
    horario = models.CharField(
        max_length=3,
        choices=HORARIOS,
        default='7-8')
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    alumno = models.ManyToManyField(Alumno)

    def __str__(self):
        return self.nombre
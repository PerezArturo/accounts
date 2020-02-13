from django.db import models
from .validators import validate_email
SEMESTRES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ]
    
class Alumno(models.Model):
    matricula = models.CharField(max_length=6,null = False, unique=True)
    nombre = models.CharField(max_length=50,null = False)
    apellidop = models.CharField(max_length=50,null = False)
    apellidom = models.CharField(max_length=50,null = False)
    email = models.EmailField(max_length=254,null = False)
    semestre = models.CharField(
        max_length=2,
        choices=SEMESTRES,
        default='1')
    
    def __str__(self):
        return self.matricula+"-"+self.apellidop+" "+self.apellidom+" "+self.nombre
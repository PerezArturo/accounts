from django.db import models

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
    matricula = models.CharField(max_length=6)
    nombre = models.CharField(max_length=50)
    apellidop = models.CharField(max_length=50)
    apellidom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    semestre = models.CharField(
        max_length=2,
        choices=SEMESTRES,
        default='1')
    
    def __str__(self):
        return self.matricula+"-"+self.apellidop+" "+self.apellidom+" "+self.nombre
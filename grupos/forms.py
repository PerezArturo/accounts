from django.forms import ModelForm, TextInput
from django import forms
from .models import Grupo
from materias.models import Materia
from salones.models import Salon
from alumnos.models import Alumno

class PostForm(ModelForm):
    HORARIOS = [
    ('7-8', '7-8'),
    ('8-9', '8-9'),
    ('9-10', '9-10'),
    ('10-11', '10-11'),
    ('11-12', '11-12'),
    ('12-1', '12-1'),
    ] 
    nombre = forms.CharField(
        widget = forms.TextInput())
    horario = forms.ChoiceField(choices=HORARIOS,widget=forms.Select())
    salon = forms.ModelChoiceField(queryset=Salon.objects.all())
    materia = forms.ModelChoiceField(queryset=Materia.objects.all())
    alumno = forms.ModelMultipleChoiceField(queryset=Alumno.objects.all())

    class Meta:
        model = Grupo
        fields = "__all__"
        
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Alumno

class PostForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = "__all__"
        labels = {
            "apellidop": _("Apellido Paterno"),
            "apellidom": _("Apellido Materno"),
        }


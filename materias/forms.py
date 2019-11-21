from django import forms
from .models import Materia

class PostForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = "__all__"
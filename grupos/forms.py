from django.forms import ModelForm, TextInput
from .models import Grupo

class PostForm(ModelForm):
    class Meta:
        model = Grupo
        fields = "__all__"
        widgets = {
            'nombre': TextInput(attrs={'size': 10, 'title': 'Search',}),
        }
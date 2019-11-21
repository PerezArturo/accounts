from django import forms
from .models import Salon

class PostForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = "__all__"
from django.forms import ModelForm, NumberInput
from django import forms
from .models import Salon

class PostForm(forms.ModelForm):

    nombre = forms.CharField(widget = forms.NumberInput())
    class Meta:
        model = Salon
        fields = "__all__"

    def clean(self):
        super(PostForm, self).clean()
        
        nombre = self.cleaned_data.get('nombre')
        

        # conditions to be met for the username length 
        if nombre is None: 
            self._errors['nombre'] = self.error_class([ 
                'Campo obligatorio'])

        # return any errors if found 
        return self.cleaned_data
from django import forms
from .models import Materia

class PostForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = "__all__"

    
    def clean(self):
        super(PostForm, self).clean()
        
        nombre = self.cleaned_data.get('nombre')
        semestre = self.cleaned_data.get('semestre')
        

        # conditions to be met for the username length 
        if nombre is None: 
            self._errors['nombre'] = self.error_class([ 
                'Campo obligatorio'])
        if semestre is None: 
            self._errors['semestre'] = self.error_class([ 
                'Campo obligatorio'])

        # return any errors if found 
        return self.cleaned_data

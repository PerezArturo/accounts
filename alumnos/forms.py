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

    def clean(self):
        super(PostForm, self).clean()
        
        matricula = self.cleaned_data.get('matricula') 
        nombre = self.cleaned_data.get('nombre')
        apellidop = self.cleaned_data.get('apellidop')
        apellidom = self.cleaned_data.get('apellidom')
        email = self.cleaned_data.get('email')

        # conditions to be met for the username length 
        if matricula is None or len(matricula) < 6: 
            self._errors['matricula'] = self.error_class([ 
                'Campo obligatorio | Debe de contener 6 caracteres']) 
        if nombre is None: 
            self._errors['nombre'] = self.error_class([ 
                'Campo obligatorio'])
        if apellidop is None: 
            self._errors['apellidop'] = self.error_class([ 
                'Campo obligatorio'])
        if apellidom is None: 
            self._errors['apellidom'] = self.error_class([ 
                'Campo obligatorio'])
        if email is None: 
            self._errors['email'] = self.error_class([ 
                'Campo obligatorio'])

        # return any errors if found 
        return self.cleaned_data


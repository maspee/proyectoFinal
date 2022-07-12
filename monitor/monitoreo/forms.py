from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre', 'rut', 'edad', 'correo', 'direccion', 'telefono', 'imagen', 'descripcion']
        
    
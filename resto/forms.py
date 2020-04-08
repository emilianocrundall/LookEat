from django import forms
from .models import Plato

class EditarForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre', 'categoria', 'imagen', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control2'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control2'}),
            'imagen': forms.FileInput(),
        }

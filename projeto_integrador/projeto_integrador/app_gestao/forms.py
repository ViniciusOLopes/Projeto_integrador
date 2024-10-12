from django import forms
from .models import Usuarios

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'  # Inclui todos os campos do modelo no formulário
        widgets = {
            'Emissao': forms.DateInput(attrs={'type': 'date'}),
            'Data_Nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

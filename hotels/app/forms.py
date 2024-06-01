from django.forms import ModelForm, EmailInput
from app.models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }
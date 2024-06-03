from django.forms import ModelForm, EmailInput
from app.models import Usuario, Vuelo, Reseña

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }

class VueloForm(ModelForm):
    class Meta:
        model = Vuelo
        fields = ['usuario', 'origen', 'destino', 'fecha_salida', 'fecha_regreso']

class ReseñaForm(ModelForm):
    class Meta:
        model = Reseña
        fields = ['usuario', 'hotel', 'texto', 'puntuacion']
from django.forms import ModelForm, widgets
from .models import Juego

class JuegoForm(ModelForm):

    class Meta:
        model = Juego
        fields = '__all__'

        
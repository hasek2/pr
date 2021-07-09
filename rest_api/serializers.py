from rest_framework import serializers
from core.models import Juego

class JuegoSerializer(serializers.ModelSerializer):
    nombre_desarrollador = serializers.CharField(read_only=True, source="desarrollador.nombre_desarrollador")
    class Meta:
        model = Juego
        fields = '__all__'
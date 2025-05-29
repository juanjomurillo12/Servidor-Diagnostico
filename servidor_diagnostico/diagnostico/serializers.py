from rest_framework import serializers
from .models import Diagnostico

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = ['id', 'paciente', 'comentarios', 'cirugia', 'creado_en']

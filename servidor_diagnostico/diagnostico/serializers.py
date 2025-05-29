# diagnostico/serializers.py
from rest_framework import serializers
from .models import Diagnostico

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = ['id', 'paciente_id', 'comentarios', 'cirugia', 'creado_en']
        read_only_fields = ['id', 'creado_en']

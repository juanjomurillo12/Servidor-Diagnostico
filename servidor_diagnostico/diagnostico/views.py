# diagnostico/views.py
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Diagnostico
from .serializers import DiagnosticoSerializer

@method_decorator(csrf_exempt, name="dispatch")
class DiagnosticoViewSet(viewsets.ModelViewSet):
    """
    Ahora cualquiera puede hacer POST/GET/etc a /diagnosticos/
    """
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer
    permission_classes = [AllowAny]

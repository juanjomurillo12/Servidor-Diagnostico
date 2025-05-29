# diagnostico/views.py
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Diagnostico
from .serializers import DiagnosticoSerializer

@method_decorator(csrf_exempt, name="dispatch")
class DiagnosticoViewSet(viewsets.ModelViewSet):
    """
    Ahora este ViewSet ya no exigirá token CSRF en peticiones POST/PUT/DELETE.
    """
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # si quieres que cada usuario sólo vea sus propios diagnósticos:
        return Diagnostico.objects.filter(paciente=self.request.user)

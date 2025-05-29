from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Diagnostico
from .serializers import DiagnosticoSerializer

class DiagnosticoViewSet(viewsets.ModelViewSet):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # si deseas filtrar por paciente autenticado
        user = self.request.user
        return Diagnostico.objects.filter(paciente=user)
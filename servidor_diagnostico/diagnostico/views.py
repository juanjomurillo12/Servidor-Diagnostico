# diagnostico/views.py
from rest_framework import viewsets
from rest_framework.permissions    import AllowAny
from rest_framework.authentication import SessionAuthentication
from .models       import Diagnostico
from .serializers  import DiagnosticoSerializer

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        # skip CSRF check
        return

class DiagnosticoViewSet(viewsets.ModelViewSet):
    queryset             = Diagnostico.objects.all()
    serializer_class     = DiagnosticoSerializer
    permission_classes   = [AllowAny]
    authentication_classes = [CsrfExemptSessionAuthentication]

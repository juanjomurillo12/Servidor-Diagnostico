# diagnostico/views.py

from rest_framework import viewsets
from rest_framework.permissions    import AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework.parsers       import JSONParser
from .models       import Diagnostico
from .serializers  import DiagnosticoSerializer

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # desactiva CSRF

class DiagnosticoViewSet(viewsets.ModelViewSet):
    queryset               = Diagnostico.objects.all()
    serializer_class       = DiagnosticoSerializer
    permission_classes     = [AllowAny]
    authentication_classes = [CsrfExemptSessionAuthentication]
    parser_classes         = [JSONParser]

    def create(self, request, *args, **kwargs):
        # imprime en consola lo que llega
        print("=== REQUEST.DATA ===", request.data)
        return super().create(request, *args, **kwargs)

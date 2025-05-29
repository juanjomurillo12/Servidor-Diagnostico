from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Diagnostico(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diagnosticos')
    comentarios = models.TextField(blank=True)
    cirugia = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diagnostico #{self.id} para {self.paciente}"  
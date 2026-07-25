from django.db import models
from django.contrib.auth.models import User


class Resena(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    calificacion_comida = models.IntegerField()
    calificacion_servicio = models.IntegerField()
    comentario = models.TextField(max_length=500)

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.usuario.username} - Comida: {self.calificacion_comida} | Servicio: {self.calificacion_servicio}"
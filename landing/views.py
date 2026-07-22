from django.shortcuts import render
from comentarios.models import Resena  # <--- Importa tu modelo desde la app de comentarios
from usuarios.decorador import verificar


def home(request):
    # 1. Traemos todas las reseñas de la base de datos (Las tienes tal cual las dejó Miguel)
    todas_las_resenas = Resena.objects.all().order_by('-fecha')

    # 2. Preparamos el contexto original de Miguel
    contexto = {
        'reseñas': todas_las_resenas
    }

    # 3. Lógica corregida para que cargue la Landing pública por defecto:
    usuario_actual = request.session.get("logueado")

    # Validamos con seguridad si el usuario existe y si su rol es admin
    if usuario_actual and usuario_actual.get("rol") == "admin":
        return render(request, 'landing/inicio_admin.html', contexto)

    # Si no ha iniciado sesión, o es cliente, va directo a la landing del usuario
    return render(request, 'landing/landing.html', contexto)
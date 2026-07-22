from django.urls import path
from . import views
app_name = 'comentarios'

urlpatterns = [
    path('comentarios/', views.crear_resena, name='crear_resena'),
]

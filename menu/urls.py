from django.urls import path
from . import views


urlpatterns = [
    path('', views.ver_carta, name='ver_carta'),
    path('crear_plato', views.crear_plato, name='crear_plato')
]

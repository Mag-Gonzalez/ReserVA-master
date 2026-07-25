from django.shortcuts import render, redirect


def ver_carta(request):
    return render(request, "menu/carta.html")

def crear_plato(request):
    return render(request,"menu/crear_plato.html")



def actualizar_plato(request):
    pass

def eliminar_plato(request):
    pass
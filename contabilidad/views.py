from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Movimiento

#Esta es la parte principal, aca mostraremos todos los gastos, ganancias ETC
def inicio(request):

    gastos = Movimiento.objects.all()


    gasto_total = 0
    gasto_efectivo = 0
    gasto_banco = 0

    for g in gastos:
        gasto_total += g.valor


        metodo = g.metodo_pago.strip().lower()

        if metodo == "efectivo":
            gasto_efectivo += g.valor

        elif "tarjeta" in metodo or "transferencia" in metodo or "débito" in metodo or "crédito" in metodo:
            gasto_banco += g.valor


    q = {
        'gastos': gastos,
        'gasto_total': gasto_total,
        'gasto_efectivo': gasto_efectivo,
        'gasto_banco': gasto_banco
    }

    return render(request, "contabilidad/prueba.html", q)

def control_gastos(request):
    return render(request, "contabilidad/control_gastos.html")

def guardar_gasto(request):
    if request.method == "POST":
        concepto = request.POST.get("concepto")
        categoria = request.POST.get("categoria")
        valor = request.POST.get("valor")
        metodo_pago = request.POST.get("metodo_pago")

        Movimiento.objects.create(
            concepto=concepto,
            categoria=categoria,
            valor=valor,
            metodo_pago=metodo_pago
        )
        messages.success(request, "¡Gasto Registrado con Éxito!!")
        return redirect('control_gastos')


    return redirect('inicio_contabilidad')

def eliminar_gasto(request,id):
    g = Movimiento.objects.get(pk=id)
    g.delete()
    return redirect('inicio_contabilidad')

def editar_gasto(request, id):
    g = Movimiento.objects.get(id=id)
    if request.method=="POST":
        g.concepto = request.POST.get('concepto')
        g.categoria = request.POST.get('categoria')
        g.valor = request.POST.get('valor')
        g.fecha = request.POST.get('fecha')
        g.metodo_pago = request.POST.get('metodo_pago')

        return redirect('contabilidad/guardar_gasto')

    else:
        g = Movimiento.objects.get(pk=id)
        contexto = {
            "gasto": g
        }
        return render(request, "contabilidad/editar_gasto.html", contexto)




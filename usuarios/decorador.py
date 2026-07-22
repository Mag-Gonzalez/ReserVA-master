from django.shortcuts import redirect

def verificar(func):
    def vigilante(request, *args, **kwargs):
        if not request.session.get("logueado", False):
            return redirect ('inicio')
        return func(request, *args, **kwargs)
    return vigilante

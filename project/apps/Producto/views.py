from django.shortcuts import render


# Create your views here.

def index(request):
    contexto = {"APP": "Aplicion Producto"}
    return render(request, "producto/Producto.html", context=contexto)
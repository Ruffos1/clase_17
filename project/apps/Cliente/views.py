from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date
from.models import Cliente, Pais
from .forms import ClienteForm

# Create your views here.

def index(request):
    clientes_registros = Cliente.objects.all() 
    """Esta funcion muestra los objetos de un modelo"""
    contexto = {"Clientes": clientes_registros}
    return render(request, "cliente/index.html", context=contexto)

def cliente(request):
    from datetime import date
    p1 = Pais(nombre="Peru")
    p2 = Pais(nombre="Australia")
    c1 = Cliente(nombre="Almendra", apellido="Ruiseñor", nacimiento = date(2015,1,1), pais_origen_id = p1)
    c2 = Cliente(nombre="Americo", apellido= "Rosales", nacimiento = date(2006,9,11), pais_origen_id = p2)
    p1.save()
    p2.save()
    
    c1.save()
    c2.save()

    
    "Esto sirve para guardar automaticamente datos en la base"
    return redirect("Cliente:Home")

"Funcion para crear forms"
def crear_cliente(request : HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ClienteForm(request.POST)
        #Indiaca que esta variable debe guardarse
        if form.is_valid():
            form.save()
            return redirect("Cliente:Home")
    else: #request.method == "GET"
        form = ClienteForm()

    return render(request, "cliente/crear.html", context= {"form": form})

def busqueda(request : HttpRequest) -> HttpResponse:
    #Busqueda por nombre
    cliente_nombre = Cliente.objects.filter(nombre__contains = "Matias")
    #Buscar los que tienen un pais vacio
    cliente_pais = Cliente.objects.filter(pais_origen_id=None)
    #Busqueda por nacimiento (mayor a los 2000)
    cliente_nacimiento = Cliente.objects.filter(nacimiento__gt = date(2000,1,1))
    contexto ={"cliente_nombre":cliente_nombre,
        "cliente_nacimiento":cliente_nacimiento,
        "sin_pais": cliente_pais}
    return render(request, "cliente/search.html", contexto)

from django.shortcuts import render, redirect
from.models import Cliente, Pais

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
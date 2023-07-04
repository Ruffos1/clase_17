from django.http import HttpResponse
#from django.template import Context, Template
from django.shortcuts import render
from datetime import datetime
def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<h1> Segunda Vista </h1>")

def nombre(request, nombre:str, apellido:str):
    nombre = nombre.capitalize()
    apellido = apellido.upper()
  
    return HttpResponse(f"{apellido}, {nombre}")

def probando_template(request):
    #mi_html = open("./templates/template1.html")
    #mi_template= Template(mi_html.read())
    #mi_html.close()
    nombre = "Matias"
    apellido = "Landoni"
    ahora = datetime.now().strftime(r"%d/%m/%Y")
    mis_datos = {"Nombre" : nombre, "Apellido" : apellido} 
    mis_datos["Fecha"]= ahora
    #mi_contexto = Context(mis_datos)
    #mi_documento= mi_template.render(mi_contexto)
    #return HttpResponse(mi_documento)
    return render(request, "template1.html", context=mis_datos)

notas = [6, 7, 5, 10, 9, 9, 8]
def desafio(request):
    mis_notas= notas
    contexto= {"Notas": mis_notas}
    return render(request, "notas.html", context=contexto)

def promedio(request):
    suma = sum(notas)
    
    Promedio = suma / len(notas)
    contexto = {"Promedio": Promedio}
    return render(request, "template2.html", context=contexto)
    
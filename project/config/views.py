from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<h1> Segunda Vista </h1>")
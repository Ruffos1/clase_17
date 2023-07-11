from django.urls import path
"""Include llama urls de otras apps"""
from .views import index, cliente, crear_cliente, busqueda
app_name="Cliente"
urlpatterns = [
    path("", index, name="Home" ),
    path("clientes_predeterminados/", cliente, name = "clientes"  ),
    path("crear/", crear_cliente, name="crear"),
    path("search/", busqueda, name="search")
    
]
"Cda funcion cread se le agregara una urls"
from django.urls import path
"""Include llama urls de otras apps"""
from .views import index, cliente
app_name="Cliente"
urlpatterns = [
    path("", index, name="Home" ),
    path("clientes_predeterminados/", cliente, name = "clientes"  )
    
]
"Cda funcion cread se le agregara una urls"
"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
"""Include llama urls de otras apps"""
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("clientes/", include("Cliente.urls") ),
    path("saludar/", views.saludo),
    path("vista2/", views.segunda_vista),
    path("persona/<apellido>/<nombre>/", views.nombre),
    path("probando_templates/",views.probando_template ),
    path("notas/", views.desafio),
    path("promedio/", views.promedio),
    path("producto/",  include("Producto.urls")),
    path("home/", include("Home.urls"))
    
]

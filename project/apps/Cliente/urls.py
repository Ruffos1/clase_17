from django.urls import path
"""Include llama urls de otras apps"""
from .views import index
app_name="Cliente"
urlpatterns = [
    path("", index, name="Home" ),
    
]

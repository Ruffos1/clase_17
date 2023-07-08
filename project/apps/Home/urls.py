from django.urls import path
"""Include llama urls de otras apps"""
from .views import home
app_name = "Home"
urlpatterns = [
    path("", home, name="Home" ),
    
]
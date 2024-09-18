from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio, name="inicio"),
    path("mostra_familia",views.mostra_familia,name="mostra_familia"),
]
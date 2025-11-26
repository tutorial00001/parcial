from django.urls import path
from . import views

urlpatterns = [
path("support/",views.plantilla, name = "vistacontac"),

path("principal/",views.planilla, name = "mainvista"),
]

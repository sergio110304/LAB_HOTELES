from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bienvenido(request):
    return HttpResponse("Bienvenido a la aplicación de hoteles")

from django.shortcuts import render
from django.http import HttpResponse
from Familia.models import Listado

# Create your views here.

def lista_familia(request):
    familia = Listado.objects.all()
    lista_familia_nombres = []
    for listado in familia:
        lista_familia_nombres.append(listado.familiar)
        lista_familia_nombres.append(listado.nombre)
        lista_familia_nombres.append(listado.nacimiento)
    return HttpResponse (lista_familia_nombres)

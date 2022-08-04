from http import HTTPStatus
from re import template
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime

def index(request):
    # paso0 : Crear contexto
    datos = {"index": [1,2,3], "familia": "FiorellaPaniagua"}
    #paso1: Cargar contenido HTML
    archivo = open(r"C:\Users\User\Downloads\python\clase 18\MVTFiorellaPaniagua\MVTFiorella\MVTFiorella\templates\index.html", "r")
    contenido = archivo.read()
    archivo.close()
    #paso2: Crear la plantilla
    plantilla = Template(contenido)
    #paso3: Crear el contexto
    contexto = Context(datos)
    #paso4: Renderizar el HTML con la informacion del contexto
    documento = plantilla.render(contexto)
    #paso5: Devolver la respuesta al usuario
    return HttpResponse(documento)
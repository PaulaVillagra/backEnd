from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def saludo(request):
    return HttpResponse("<h1>Hola</h1>")
def hora(request):
    dt=datetime.datetime.now()
    s="<b>Fecha y Hora Actual: </b>"+str(dt)
    return HttpResponse(s)
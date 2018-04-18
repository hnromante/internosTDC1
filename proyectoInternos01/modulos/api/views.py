from django.shortcuts import render
from rest_framework import viewsets
from modulos.models import Modulo
from .serializers import ModuloSerializer


# Create your views here.

"""
ModelViewSet se encarga de incorporar las funciones más básicas que va a necesitar un Modelo,
para GET, PUT, DELETE
"""
class ModuloView(viewsets.ModelViewSet):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer



def index(request):
    return render(request, 'index.html')
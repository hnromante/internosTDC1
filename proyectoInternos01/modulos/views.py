from django.shortcuts import render
from rest_framework import viewsets
from .models import Modulo, User
from .serializers import ModuloSerializer, UsuarioSerializer

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )


# Create your views here.

"""
ModelViewSet se encarga de incorporar las funciones más básicas que va a necesitar un Modelo,
para GET, PUT, DELETE
"""
class ModuloView(viewsets.ModelViewSet):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

def index(request):
    return render(request, 'index.html')
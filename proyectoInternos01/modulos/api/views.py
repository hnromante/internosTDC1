from rest_framework import viewsets
from modulos.models import Modulo
from .serializers import (
    ModuloSerializer, 
    ModuloListSerializer,
    ModuloCrearActualizarSerializer,
    ModuloDetalleSerializer
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView
)

#IMPORT PERMISOS
from rest_framework.permissions import AllowAny
class ModuloViewset(viewsets.ModelViewSet):
    """
    Viewset Generico que soporta todos los métodos HTTP [GET,POST,PUT,PATCH,DELETE,ETC].
    Vamos a dividirlo en API ENDPOINTS diferentes para cada operación.
    """
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer


class ModuloListView(ListAPIView):
    """
    View que permite solo leer la lista de modulos 
    """
    queryset = Modulo.objects.all()
    serializer_class = ModuloListSerializer
    permission_classes = [AllowAny]

class ModuloCreateView(CreateAPIView):
    """
    View que permite un POST (crear) un modulo
    """
    queryset = Modulo.objects.all() #??
    serializer_class = ModuloCrearActualizarSerializer
    permission_classes = [AllowAny]

class ModuloDetalleView(RetrieveAPIView):
    """
    View para ver el detalle de un modulo, a traves del ID(pk)
    """
    queryset = Modulo.objects.all()
    serializer_class = ModuloDetalleSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
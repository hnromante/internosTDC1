from cuentas.models import User
from rest_framework import viewsets
<<<<<<< HEAD
from rest_framework import views
from .serializers import UsuarioSerializer
=======
from .serializers import UsuarioSerializer, UsuarioCrearSerializer, UsuarioListarSerializer, UsuarioDetalleSerializer
from rest_framework.permissions import AllowAny
>>>>>>> 19bdee956422a982e2bd38a0cb00a97fa0ae1cb4


from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)

class UserViewAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioCrearAPI(CreateAPIView):
    serializer_class = UsuarioCrearSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

class UsuarioListarAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioListarSerializer
    permission_classes = [AllowAny]

class UsuarioDetalleAPI(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioDetalleSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]



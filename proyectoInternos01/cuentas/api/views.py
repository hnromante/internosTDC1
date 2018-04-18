from cuentas.models import User
from rest_framework import viewsets
from .serializers import UsuarioSerializer, UsuarioCrearSerializer, UsuarioListarSerializer, UsuarioDetalleSerializer
from rest_framework.permissions import AllowAny


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



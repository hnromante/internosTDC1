from cuentas.models import User
from rest_framework import viewsets
from .serializers import (
    UsuarioSerializer, 
    UsuarioCrearActualizarSerializer, 
    UsuarioListarSerializer, 
    UsuarioDetalleSerializer,
)
from rest_framework.permissions import AllowAny


from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)

class UserAPIViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioCrearAPIView(CreateAPIView):
    serializer_class = UsuarioCrearActualizarSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

class UsuarioListarAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioListarSerializer
    permission_classes = [AllowAny]

class UsuarioDetalleByIdAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioDetalleSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class UsuarioDetalleByEmailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioDetalleSerializer
    lookup_field = 'email'
    permission_classes = [AllowAny]

class UsuarioEditarAPIView(RetrieveUpdateAPIView):
    """
    Serializador para editar un USUARIO por ID
    """
    queryset = User.objects.all()
    serializer_class = UsuarioCrearActualizarSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email

class UsuarioEliminarAPIView(DestroyAPIView):
    """
    Serializador par eliminar un usuario por ID
    """
    queryset = User.objects.all()
    serializer_class = UsuarioDetalleSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    #lookup_url_kwarg = "abc"
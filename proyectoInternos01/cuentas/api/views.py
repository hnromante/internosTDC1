from cuentas.models import User
from rest_framework import viewsets
from rest_framework import views
from .serializers import UsuarioSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
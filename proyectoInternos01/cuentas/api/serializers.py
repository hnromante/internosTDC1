 
#from rest_framework import serializers
from cuentas.models import User


from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')


class UsuarioCrearActualizarSerializer(ModelSerializer):
    #email = EmailField(label = 'Email Address')
    #email2 = EmailField(label = 'Confirm Email')
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]
    #Aun sin validar
    def validar(self, data):
        pass


class UsuarioListarSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]

class UsuarioDetalleSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'password'
        ]
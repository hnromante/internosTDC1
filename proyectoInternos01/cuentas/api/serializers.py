from cuentas.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,    
    EmailField,
    CharField,
    ValidationError
)
from django.db.models import Q

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')


class UsuarioCrearActualizarSerializer(ModelSerializer):
    # email = EmailField(label = 'Email')
    #email2 = EmailField(label = 'Confirm Email')
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password'
        ]
    #Aun sin validar
    def validate(self, data):
        return data

    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username = username,
            email = email,
            first_name = first_name
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


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
            'password',
            'auth_token'
        ]


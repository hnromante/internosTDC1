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
    #email = EmailField(label = 'Email Address')
    #email2 = EmailField(label = 'Confirm Email')
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password',
            'auth_token'
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
            'password',
            'auth_token'
        ]
# class UsuarioLoginSerializer(ModelSerializer):
#     email = EmailField(required=True, allow_blank=False)
#     password = CharField(required=True, allow_blank=False)
#     auth_token = CharField(required=False, allow_blank=True, style={'input_type': 'hidden'})
#     first_name = CharField(required=False, allow_blank=True, style={'input_type': 'hidden'})
#     last_name = CharField(required=False, allow_blank=True, style={'input_type': 'hidden'})
#     class Meta:
#         model = User
#         fields = [
#             'id',
#             'email',
#             'first_name',
#             'last_name',
#             'password',
#             'auth_token'
#         ]
#     def validate(self, data):
#         usuario_obj = None
#         email = data.get("email", None)
#         password = data["password"]
#         if not email:
#             raise ValidationError("Ingresar usuario y contraseña")
        
#         user = User.objects.filter(
#             Q(email=email)
#         ).distinct()

#         if user.exists() and user.count() == 1:
#             usuario_obj = user.first()
#             print (usuario_obj)
#             print (usuario_obj.auth_token)
#         else:
#             raise ValidationError("Email no valido")

#         if usuario_obj:
#             if not usuario_obj.check_password(password):
#                 raise ValidationError("Las credenciales son incorrectas")

#         data["id"] = usuario_obj.id
#         data["auth_token"] = usuario_obj.auth_token
#         data["email"] = usuario_obj.email
#         data["username"] = usuario_obj.username
#         data["first_name"] = usuario_obj.first_name
#         data["last_name"] = usuario_obj.last_name
#         return data
    

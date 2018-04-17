from rest_framework import serializers
from .models import Modulo, User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email')


class ModuloSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(many=True, read_only=True)
    class Meta:
        model = Modulo
        fields = ('id','usuario','url','nombre','subtitulo','descripcion','img')



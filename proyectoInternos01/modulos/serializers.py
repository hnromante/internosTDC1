from rest_framework import serializers
from .models import Modulo, User

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')


class ModuloSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UsuarioSerializer(many=True, read_only=True)
    class Meta:
        model = Modulo
        fields = ('id','usuario','url','nombre','subtitulo','descripcion','img')




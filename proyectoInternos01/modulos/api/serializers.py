from rest_framework import serializers
from modulos.models import Modulo

from cuentas.api.serializers import UsuarioSerializer


class ModuloSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UsuarioSerializer(many=True, read_only=True)
    class Meta:
        model = Modulo
        fields = ('id','usuario','url','nombre','subtitulo','descripcion','img')




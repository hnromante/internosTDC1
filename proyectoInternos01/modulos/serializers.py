from rest_framework import serializers
from .models import Modulo


class ModuloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Modulo
        fields = ('id','url','nombre','descripcion','img')
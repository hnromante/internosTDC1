from rest_framework import serializers
from cuentas.models import User

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')
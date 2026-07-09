from administrativo.models import TipoDireccion
from django.contrib.auth.models import User, Group
from administrativo.models import *

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EstudianteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


class NumeroTelefonicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NumeroTelefonico
        # fields = ['id', 'telefono', 'tipo']
        fields = '__all__'

class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        # fields = ['id', 'direccion']
        fields = '__all__'

class TipoDireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoDireccion
        # fields = ['id', 'tipo']
        fields = '__all__'

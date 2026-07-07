from administrativo.models import TipoEstudiante
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

class DescripcionEstudianteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DescripcionEstudiante
        # fields = ['id', 'descripcion']
        fields = '__all__'

class TipoEstudianteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoEstudiante
        # fields = ['id', 'tipo']
        fields = '__all__'

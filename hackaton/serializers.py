import datetime

from .models import Hackaton
from users.models import Equipos
from rest_framework import serializers
from django.utils.timezone import now


class HackatonSerializer(serializers.HyperlinkedModelSerializer):
    paso = serializers.SerializerMethodField()
    fecha_format = serializers.SerializerMethodField()

    def get_fecha_format(self, obj):
        obj.fecha_format = "%s-%s-%s" %(obj.fecha.day, obj.fecha.month, obj.fecha.year)
        return obj.fecha_format


    def get_paso(self, obj):

        obj.si = (obj.fecha - now()).days
        print ("Hola %d" % obj.si)

        if obj.si <= 0:
            obj.paso = 1
        else:
            obj.paso = 0

        return obj.paso

    class Meta:
        model = Hackaton
        fields = ('id', 'nombreHackaton', 'lugar', 'fecha_format', 'paso', 'descripcion')


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipos
        fields = ('nombreProyecto',)

class HackatonDetailSerializer(serializers.HyperlinkedModelSerializer):
    equipazo = serializers.HyperlinkedIdentityField(view_name='hackaton-equipos', lookup_field='id')

    class Meta:
        model = Hackaton
        fields = ('fecha', 'equipazo', 'nombreHackaton', 'descripcion' '')
import datetime

from .models import Hackaton, Sponsor
from users.models import Equipos, Lenguaje
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
        fields = ('id', 'nombreProyecto', 'descripcionProyecto', 'nombreEquipo')

class SponsorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('nombre', 'logo', 'pagina')

class HackatonDetailSerializer(serializers.HyperlinkedModelSerializer):
    equipazo = serializers.HyperlinkedIdentityField(view_name='hackaton-equipos', lookup_field='id')
    mis_sponsors = serializers.HyperlinkedIdentityField(view_name='sponsors-list', lookup_field='id')

    class Meta:
        model = Hackaton
        fields = ('fecha', 'equipazo', 'nombreHackaton', 'descripcion', 'lugar', 'mis_sponsors')



class EquiposBusqueda(serializers.ModelSerializer):
#    tecnologias = serializers.HyperlinkedRelatedField(
#        many=True,
#        read_only=True,
#        view_name='equipos-busqueda'
#    )

    class Meta:
        model = Equipos
        fields = ('nombreEquipo', 'nombreProyecto', 'tecnologias', 'id')


class TechListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lenguaje
        fields=('nombreLenguaje',)

class EquipoDetailSerializer(serializers.HyperlinkedModelSerializer):
    tech = serializers.HyperlinkedIdentityField(view_name='tech-list', lookup_field='id')
    class Meta:
        model = Equipos
        fields = ('id', 'nombreProyecto', 'descripcionProyecto', 'nombreEquipo', 'tech', 'github', 'url')



class BuscarCoder(serializers.ModelSerializer):

    class Meta:
        model = Coder
        fields = ('participantes', 'id')

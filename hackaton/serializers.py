from .models import Hackaton
from rest_framework import serializers
from django.utils.timezone import now


class HackatonSerializer(serializers.HyperlinkedModelSerializer):
    paso = serializers.SerializerMethodField()

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
        fields = ('id', 'nombreHackaton', 'lugar', 'fecha', 'paso')
from .models import Hackaton
from rest_framework import serializers


class HackatonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Hackaton
        fields = ('id', 'nombreHackaton',)
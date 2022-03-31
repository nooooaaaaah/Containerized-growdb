from rest_framework import serializers

from growop.models import Plant

class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'name', 'seed', 'clone', 'tent' , 'cycle')
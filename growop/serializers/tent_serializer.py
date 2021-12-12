from rest_framework import serializers

from growop.models import Tent
from growop.models import Cycle

class TentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tent
        cycle = Cycle
        fields = ('id', 'name', 'cycle', 'lightWatts', 'numOfLights')

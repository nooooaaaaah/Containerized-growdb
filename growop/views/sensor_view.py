from rest_framework import viewsets

from growop.serializers import SensorSerializer
from growop.models import Sensor

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
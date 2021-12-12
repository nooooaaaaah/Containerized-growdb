from rest_framework import viewsets

from growop.serializers import Sensor_DataSerializer
from growop.models import Sensor_Data

class Sensor_DataViewSet(viewsets.ModelViewSet):
    queryset = Sensor_Data.objects.all()
    serializer_class = Sensor_DataSerializer
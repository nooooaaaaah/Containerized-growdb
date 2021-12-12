from rest_framework import viewsets

from growop.serializers import PlantSerializer
from growop.models import Plant

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
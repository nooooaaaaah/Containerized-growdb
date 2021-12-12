# Create your views here.
from rest_framework import viewsets

from growop.serializers import CycleSerializer
from growop.models import Cycle


class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer
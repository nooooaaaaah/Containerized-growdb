from rest_framework import viewsets

from growop.serializers import TentSerializer
from growop.models import Tent

class TentViewSet(viewsets.ModelViewSet):
    queryset = Tent.objects.all()
    serializer_class = TentSerializer
from django.db import models
from .tent_model import Tent
from .cycle_model import Cycle

class Plant(models.Model):
    name = models.CharField(max_length=60)
    id = models.AutoField(primary_key=True)
    seed = models.BooleanField(default=False)
    clone = models.BooleanField(default=False)
    tent = models.ForeignKey(Tent, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
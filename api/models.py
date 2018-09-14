from django.db import models

# Create your models here.
class CharityLot(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True)

    base_cost = models.IntegerField(default=0)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)

    def __str__(self):
        return str(self.name)

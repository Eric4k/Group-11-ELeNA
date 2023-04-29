from django.db import models

# Create your models here.

class Location(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return f"({self.lat}, {self.lon})"

from django.db import models
from django.contrib.auth.models import AbstractUser


# create your models here.

class Location(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return f"({self.lat}, {self.lon})"


#use django's built-in Abstract User that has necessary fields such as username, email, password
class CustomUser(AbstractUser):
    pass
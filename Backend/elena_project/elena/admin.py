from django.contrib import admin
from .models import Location
from .models import CustomUser

# register your models here.
admin.site.register(Location)
admin.site.register(CustomUser)



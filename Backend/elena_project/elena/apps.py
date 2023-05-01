from django.apps import AppConfig
from geoDataRetriever import initializeGeoDataGraphs

class ElenaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'elena'
    def ready(self):
        #initialize the graphs when the server is started
        initializeGeoDataGraphs()
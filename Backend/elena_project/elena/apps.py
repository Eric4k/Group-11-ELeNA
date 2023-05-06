from django.apps import AppConfig
from . import geoDataRetriever
from pathlib import Path
import os
from . import routeProcessing

class ElenaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'elena'
    def ready(self):
        # to avoid running more than once, only run during runserver
        if os.environ.get('RUN_MAIN'):
            # check if the dataSet folder already exist then don't run inititalize
            dirExist = Path("dataSets");
            if not dirExist.is_dir():
                geoDataRetriever.initializeGeoDataGraphs()
            else:
                geoDataRetriever.loadGraphMLData()
                print("loaded")
                routeProcessing.test_astar()
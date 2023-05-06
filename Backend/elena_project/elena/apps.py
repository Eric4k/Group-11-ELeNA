from django.apps import AppConfig
from .geoDataRetriever import initializeGeoDataGraphs, loadGraphMLData
from .routeProcessing import test_astar
from pathlib import Path
import os


class ElenaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'elena'
    def ready(self):
        # to avoid running more than once, only run during runserver
        if os.environ.get('RUN_MAIN'):
            # check if the dataSet folder already exist then don't run inititalize
            dirExist = Path("dataSets");
            if not dirExist.is_dir():
                initializeGeoDataGraphs()
            else:
                #TODO does not wait for data to load needs fix
                loadGraphMLData()
                print("loaded")
                # testing
                # test_astar()
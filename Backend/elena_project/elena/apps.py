from django.apps import AppConfig
from .geoDataRetriever import initializeGeoDataGraphs, loadGraphMLData, getBikingData, getWalkingData
from pathlib import Path
import os
from .routingAlgorithms import Astar, algorithmSelection


class ElenaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'elena'
    def ready(self):
         # specifies the file to search for
        city = 'Amherst'
        state = 'MA'
        # to avoid running more than once, only run during runserver
        if os.environ.get('RUN_MAIN'):
            
            # check if the dataSet folder already exist then don't run inititalize
            city_walk_graph_exist = Path(f"dataSets/{city}_{state}_Walk.graphml")
            city_bike_graph_exist = Path(f"dataSets/{city}_{state}_Bike.graphml")
            
            # if file does not exist create it
            if not city_walk_graph_exist.is_file() and not city_bike_graph_exist.is_file():
                initializeGeoDataGraphs(city, state)
            
            if loadGraphMLData(city, state):
                print("loaded")
                    
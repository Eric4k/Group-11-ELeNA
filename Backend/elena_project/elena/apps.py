from django.apps import AppConfig
from .geoDataRetriever import initializeGeoDataGraphs, loadGraphMLData, getBikingData, getWalkingData
from pathlib import Path
import os
from .routingAlgorithms import Astar, algorithmSelection


class ElenaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'elena'
    def ready(self):
        # to avoid running more than once, only run during runserver
        if os.environ.get('RUN_MAIN'):
            # check if the dataSet folder already exist then don't run inititalize
            dirExist = Path("dataSets");
            if not dirExist.is_dir():
                initializeGeoDataGraphs("Amherst", "MA")
            else:
                #TODO does not wait for data to load needs fix 
                if loadGraphMLData("Amherst", "MA"):
                    print("loaded")
                    # print(getDrivingData())
                    # print(getBikingData())
                    # print(getWalkingData())
                    # source = 66705576
                    # target = 1443766572

                    # astar = Astar()
    
                    # routing = algorithmSelection(astar)
    
                    # path = routing.compute_route(getBikingData(), source, target, 80, True, 20)
                    # print(path)

                # testing
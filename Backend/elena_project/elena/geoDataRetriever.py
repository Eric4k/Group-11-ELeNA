import osmnx as ox

geoDataGraphWalk = None
geoDataGraphBike = None
geoDataGraphDrive = None

def loadGraphMLData():
    global geoDataGraphWalk
    global geoDataGraphBike
    global geoDataGraphDrive
    
    geoDataGraphWalk = ox.load_graphml("dataSets/Amherst_Walk_Data.graphml")
    geoDataGraphBike = ox.load_graphml("dataSets/Amherst_Bike_Data.graphml")
    geoDataGraphDrive = ox.load_graphml("dataSets/Amherst_Drive_Data.graphml")


# run once to create the graphs
def initializeGeoDataGraphs():
    
    #retreive the networkx graph with direct edges
    walkGraph = ox.graph_from_place("Amherst, MA", network_type='walk', simplify=False)
    #add edge travel time
    walkGraph = ox.add_edge_travel_times(ox.add_edge_speeds(walkGraph))
    #add elevation to nodes
    walkGraph = ox.add_node_elevations_google(walkGraph, None, max_locations_per_batch=100, pause_duration=2, precision=3, url_template='https://api.opentopodata.org/v1/aster30m?locations={}&key={}')
    #save to graphml file
    ox.save_graphml(walkGraph,"dataSets/Amherst_Walk_Data.graphml", gephi=False, encoding='utf-8')
    
    #retreive the networkx graph with direct edges
    bikeGraph = ox.graph_from_place("Amherst, MA", network_type='bike', simplify=False)
    #add edge travel time
    bikeGraph = ox.add_edge_travel_times(ox.add_edge_speeds(bikeGraph))
    #add elevation to nodes
    bikeGraph = ox.add_node_elevations_google(bikeGraph, None, max_locations_per_batch=100, pause_duration=2, precision=3, url_template='https://api.opentopodata.org/v1/aster30m?locations={}&key={}')
    #save to graphml file
    ox.save_graphml(bikeGraph,"dataSets/Amherst_Bike_Data.graphml", gephi=False, encoding='utf-8')
        
    #retreive the networkx graph with direct edges
    driveGraph = ox.graph_from_place("Amherst, MA", network_type='drive', simplify=False)
    #add edge travel time
    driveGraph = ox.add_edge_travel_times(ox.add_edge_speeds(driveGraph))
    #add elevation to nodes
    driveGraph = ox.add_node_elevations_google(driveGraph, None, max_locations_per_batch=100, pause_duration=2, precision=3, url_template='https://api.opentopodata.org/v1/aster30m?locations={}&key={}')
    #save to graphml file
    ox.save_graphml(driveGraph,"dataSets/Amherst_Drive_Data.graphml", gephi=False, encoding='utf-8')
    
def getBikingData():
    # if geoDataGraphBike is None:
    #     raise Exception("data not loaded")
    return geoDataGraphBike

def getWalkingData():
    # if geoDataGraphWalk is None:
    #     raise Exception("data not loaded")
    return geoDataGraphWalk

def getDrivingData():
    # if geoDataGraphDrive is None:
    #     raise Exception("data not loaded")
    return geoDataGraphDrive
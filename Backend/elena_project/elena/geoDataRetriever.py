import osmnx as ox

#initializing the different modes of transportation: walk, bike, drive
geoDataGraphWalk = None
geoDataGraphBike = None

def loadGraphMLData(city, state):
    global geoDataGraphWalk
    global geoDataGraphBike
    
    geoDataGraphWalk = None
    geoDataGraphBike = None
    
    #loading the map for each mode of transportation
    geoDataGraphWalk = ox.load_graphml(f"dataSets/{city}_{state}_Walk.graphml")
    geoDataGraphBike = ox.load_graphml(f"dataSets/{city}_{state}_Bike.graphml")
    
    #wait for data to load
    while (geoDataGraphWalk is None or geoDataGraphBike is None):
        pass
    
    return True


# run once to create the graphs
def initializeGeoDataGraphs(city, state):
    
    #retreive the networkx graph with direct edges
    walkGraph = ox.graph_from_place(f"{city}, {state}", network_type='walk', simplify=False)
    #add elevation to nodes
    walkGraph = ox.add_node_elevations_google(walkGraph, None, max_locations_per_batch=100, pause_duration=2, precision=3, url_template='https://api.opentopodata.org/v1/aster30m?locations={}&key={}')
    #save to graphml file
    ox.save_graphml(walkGraph,f"dataSets/{city}_{state}_Walk.graphml", gephi=False, encoding='utf-8')
    
    #retreive the networkx graph with direct edges
    bikeGraph = ox.graph_from_place(f"{city}, {state}", network_type='bike', simplify=False)
    #add elevation to nodes
    bikeGraph = ox.add_node_elevations_google(bikeGraph, None, max_locations_per_batch=100, pause_duration=2, precision=3, url_template='https://api.opentopodata.org/v1/aster30m?locations={}&key={}')
    #save to graphml file
    ox.save_graphml(bikeGraph,f"dataSets/{city}_{state}_Bike.graphml", gephi=False, encoding='utf-8')
        
    
def getBikingData():
    return geoDataGraphBike

def getWalkingData():
    return geoDataGraphWalk

import osmnx as ox

def loadGraphMLData(self):
    global geoDataGraphWalk
    global geoDataGraphBike
    global geoDataGraphDrive
    
    geoDataGraphWalk = ox.load_graphml()
    geoDataGraphBike = ox.load_graphml()
    geoDataGraphDrive = ox.load_graphml()

# run once to create the graphs
def initializeGeoDataGraphs(self):
    
    #retreive the networkx graph with direct edges
    walkGraph = ox.graph_from_address("Amherst, MA", network_type='walk', simplify=False)
    #add edge travel time
    walkGraph = ox.add_edge_travel_times(ox.add_edge_speeds(geoDataGraphWalk))
    #add elevation to nodes
    walkGraph = ox.add_node_elevations_google(walkGraph, None, max_locations_per_batch=100, pause_duration=2, precision=3, url_template='https://api.opentopodata.org/v1/aster30m?locations={}&key={}')
    #save to graphml file
    ox.save_graphml(walkGraph,"Backend/elena_project/elena/dataSets/Amherst_Walk_Data.graphml", gephi=False, encoding='utf-8')
    
    #retreive the networkx graph with direct edges
    bikeGraph = ox.graph_from_address("Amherst, MA", network_type='bike', simplify=False)
    #add edge travel time
    bikeGraph = ox.add_edge_travel_times(ox.add_edge_speeds(geoDataGraphBike))
    #add elevation to nodes
    bikeGraph = ox.add_node_elevations_google(bikeGraph, None, max_locations_per_batch=100, pause_duration=2, precision=3, url_template='https://api.opentopodata.org/v1/aster30m?locations={}&key={}')
    #save to graphml file
    ox.save_graphml(bikeGraph,"Backend/elena_project/elena/dataSets/Amherst_Bike_Data.graphml", gephi=False, encoding='utf-8')
        
    #retreive the networkx graph with direct edges
    driveGraph = ox.graph_from_address("Amherst, MA", network_type='drive', simplify=False)
    #add edge travel time
    driveGraph = ox.add_edge_travel_times(ox.add_edge_speeds(geoDataGraphDrive))
    #add elevation to nodes
    driveGraph = ox.add_node_elevations_google(driveGraph, None, max_locations_per_batch=100, pause_duration=2, precision=3, url_template='https://api.opentopodata.org/v1/aster30m?locations={}&key={}')
    #save to graphml file
    ox.save_graphml(driveGraph,"Backend/elena_project/elena/dataSets/Amherst_Drive_Data.graphml", gephi=False, encoding='utf-8')
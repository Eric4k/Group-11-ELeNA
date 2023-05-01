import osmnx as ox

def initializeGeoDataGraphs(self):
    global geoDataGraphWalk
    global geoDataGraphBike
    global geoDataGraphDrive
    
    #TODO add elevation processing
    geoDataGraphWalk = ox.graph_from_address("Amherst, MA", network_type='walk', simplify=False)
    geoDataGraphWalk  = ox.add_edge_travel_times(ox.add_edge_speeds(geoDataGraphWalk))
        
    geoDataGraphBike = ox.graph_from_address("Amherst, MA", network_type='bike', simplify=False)
    geoDataGraphBike  = ox.add_edge_travel_times(ox.add_edge_speeds(geoDataGraphBike))
        
    geoDataGraphDrive = ox.graph_from_address("Amherst, MA", network_type='drive', simplify=False)
    geoDataGraphDrive  = ox.add_edge_travel_times(ox.add_edge_speeds(geoDataGraphDrive))
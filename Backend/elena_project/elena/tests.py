from django.test import TestCase
import networkx as nx
import osmnx as ox
import logging
from routeProcessing import DFS, path_length, simplify_graph, path_elevation
import unittest
import networkx as nx

# test to check route processing
class TestRouteProcessing(unittest.TestCase):
    
    def setUp(self):
        self.G = ox.graph_from_place('Piedmont, California, USA', network_type='walk')
        # adding elevation data to each node in the graph using Google's Elevation API
        self.G = ox.add_node_elevations_google(self.G, None, max_locations_per_batch=100, pause_duration=2, precision=3, url_template='https://api.opentopodata.org/v1/aster30m?locations={}&key={}')  

    
    def test_DFS(self):
        logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s %(message)s') #setting up configurations
        logging.info('Running test_DFS')
    
        # setting the source and target nodes of the graph
        source = list(self.G.nodes())[0]
        target = list(self.G.nodes())[-1]

        # logging the source and target node ids
        logging.info(f'source: {source}')
        logging.info(f'target: {target}')

        # creating a dictionary of visited nodes and an empty dictionary for best path
        visited = {node: False for node in self.G.nodes}
        best_path = {}

        # calculating the shortest path and its length using Dijkstra's algorithm
        shortest_path = nx.dijkstra_path(self.G, source, target, weight='length')
        shortest_path_length = nx.shortest_path_length(self.G, source=source, target=target, weight='length')

        # setting a limit for the maximum length of the path
        limit = 90
        shortest_path_length_limit = ((limit/100) * shortest_path_length) + shortest_path_length

        path = []

        # simplifying the graph around the shortest path
        new_graph = simplify_graph(self.G, shortest_path, 3)

        # running DFS algorithm to find the path with maximum elevation gain
        max_elevation = DFS(shortest_path_length_limit, source, target, path, new_graph, visited, best_path)
        best_max_elevation = max(max_elevation.items(), key=lambda x: x[0])[1]

        # checking if the maximum elevation of the best path is less than or equal to the limit
        self.assertTrue(shortest_path_length_limit >= path_length(new_graph, best_max_elevation), "Max elevation less than or equal to limit")

if __name__ == '__main__':
    unittest.main()


# def test_DFS(G):
#     # print(G.nodes, G.edges)
#     source = list(G.nodes())[0]
#     target = list(G.nodes())[-1]

#     visited = {node: 
#     False for node in G.nodes}
#     best_path = {}

#     shortest_path = nx.dijkstra_path(G, source, target, weight='length')
#     shortest_path_length = nx.shortest_path_length(G, source=source, target=target, weight='length')

#     limit = 90
#     shortest_path_length_limit = ((limit/100) * shortest_path_length) + shortest_path_length

#     path = []

#     new_graph = routeProcessing.simplify_graph(G, shortest_path)
#     print(new_graph)
#     result = routeProcessing.DFS(shortest_path_length_limit, source, target, path, new_graph, visited, best_path)
#     max_elevation = max(result.keys())
#     assert limit >= max_elevation

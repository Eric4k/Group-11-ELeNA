from django.test import TestCase
import networkx as nx
import osmnx as ox
import logging
from routeProcessing import DFS, path_length, simplify_graph, path_elevation
import unittest
import networkx as nx

class TestRouteProcessing(unittest.TestCase):
    
    def setUp(self):
        self.G = ox.graph_from_place('Piedmont, California, USA', network_type='walk')
        self.G = ox.add_node_elevations_google(self.G, None, max_locations_per_batch=100, pause_duration=2, precision=3, url_template='https://api.opentopodata.org/v1/aster30m?locations={}&key={}')

    
    def test_DFS(self):
        logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
        logging.info('Running test_DFS')
    
        source = list(self.G.nodes())[0]
        target = list(self.G.nodes())[-1]

        logging.info(f'source: {source}')
        logging.info(f'target: {target}')

        visited = {node: False for node in self.G.nodes}
        best_path = {}

        shortest_path = nx.dijkstra_path(self.G, source, target, weight='length')
        shortest_path_length = nx.shortest_path_length(self.G, source=source, target=target, weight='length')

        limit = 90
        shortest_path_length_limit = ((limit/100) * shortest_path_length) + shortest_path_length

        path = []

        new_graph = simplify_graph(self.G, shortest_path, 3)

        max_elevation = DFS(shortest_path_length_limit, source, target, path, new_graph, visited, best_path)
        best_max_elevation = max(max_elevation.items(), key=lambda x: x[0])[1]

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

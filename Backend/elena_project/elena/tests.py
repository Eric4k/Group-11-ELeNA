from django.test import TestCase
import networkx as nx
import osmnx as ox
import logging
from .routeProcessing import DFS, DFS_With_Pruning, path_length, simplify_graph, path_elevation, astar_heuristic
from .routingAlgorithms import Astar, algorithmSelection, Dijkstra
import unittest

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


        # calculating the shortest path and its length using Dijkstra's algorithm
        shortest_path = nx.dijkstra_path(self.G, source, target, weight='length')
        shortest_path_length = nx.shortest_path_length(self.G, source=source, target=target, weight='length')

        # setting a limit for the maximum length of the path
        limit = 10
        shortest_path_length_limit = ((limit/100) * shortest_path_length) + shortest_path_length

        cutoff = ((len(shortest_path) * (limit/100))) + len(shortest_path)
        
        new_graph = simplify_graph(self.G, shortest_path, 10)

        # running DFS algorithm to find the path with maximum elevation gain
        max_elevation = DFS_With_Pruning(shortest_path_length_limit, source, target, [], new_graph, {}, cutoff, 0, False)

        # # running DFS algorithm to find the path with minimum elevation gain
        # min_elevation = DFS(shortest_path_length_limit, source, target, [], new_graph, {}, cutoffs, 0, True)

        # print("max elevation: ", max_elevation)
        # print("min elevation: ", min_elevation)

        # print("elevation", max_elevation["elevation"], "\n", max_elevation["path"], "\n", "best max elevation path length: ", path_length(new_graph, max_elevation["path"]))
        # print("elevation", min_elevation["elevation"], "\n", min_elevation["path"], "\n", "best max elevation path length: ", path_length(new_graph, min_elevation["path"]))

        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        # max_elevation_old = DFS_OLD(shortest_path_length_limit, source, target, [], new_graph, {}, cutoffs, 0)
        # best_max_elevation_old = max(max_elevation_old.items(), key=lambda x: x[0])[1]
        # print("max elevation", max(max_elevation_old.items(), key=lambda x: x[0]), "best max elevation path length: ", path_length(new_graph, best_max_elevation_old))

        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        # min_elevation_old = DFS_OLD(shortest_path_length_limit, source, target, [], new_graph, {}, cutoffs, 0)
        # best_min_elevation_old = min(min_elevation_old.items(), key=lambda x: x[0])[1]
        # print("min elevation", min(min_elevation_old.items(), key=lambda x: x[0]), "best min elevation path length: ", path_length(new_graph, best_min_elevation_old))
        # print("min def ", path_elevation(self.G, shortest_path))


        # # plotting the shortest path and the best path on a map
        # route = ox.plot_route_folium(self.G, shortest_path, popup_attribute="name", route_color='green', route_width=3)
        # route.save("map1.html")
        # route = ox.plot_route_folium(self.G, max_elevation["path"], popup_attribute="name", route_color='green', route_width=3)
        # route.save("map2.html")
        # checking if the maximum elevation of the best path is less than or equal to the limit
        self.assertTrue(shortest_path_length_limit >= path_length(self.G, max_elevation["path"]), "Max path length less than or equal to limit")


    def test_DFS_With_Astar_Max(self):
        logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s %(message)s') #setting up configurations
        logging.info('Running test_DFS_With_Astar_Max')
    
        # setting the source and target nodes of the graph
        source = list(self.G.nodes())[0]
        target = list(self.G.nodes())[-1]

        # logging the source and target node ids
        logging.info(f'source: {source}')
        logging.info(f'target: {target}')
        
        shortest_path = nx.astar_path(self.G, source, target, heuristic=astar_heuristic(self.G), weight="length")

        astarStrategy = Astar()
        algo = algorithmSelection(astarStrategy)
            
        route = algo.compute_route(self.G, source, target, 20, True, 15)
            
        self.assertTrue(path_elevation(self.G, shortest_path) <= route["net_elevation"], "Max elevation is greater than or equal to shortest path")
        
    def test_DFS_With_Astar_Min(self):
        logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s %(message)s') #setting up configurations
        logging.info('Running test_DFS_With_Astar_Min')
    
        # setting the source and target nodes of the graph
        source = list(self.G.nodes())[0]
        target = list(self.G.nodes())[-1]

        # logging the source and target node ids
        logging.info(f'source: {source}')
        logging.info(f'target: {target}')
        
        shortest_path = nx.astar_path(self.G, source, target, heuristic=astar_heuristic(self.G), weight="length")

        astarStrategy = Astar()
        algo = algorithmSelection(astarStrategy)
            
        route = algo.compute_route(self.G, source, target, 20, False, 15)
        
        self.assertTrue(path_elevation(self.G, shortest_path) >= route["net_elevation"], "Max elevation is less than or equal to shortest path")
        
    def test_DFS_With_Astar_Deviation_Zero(self):
        logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s %(message)s') #setting up configurations
        logging.info('Running test_DFS_With_Astar_Deviation_Zero')
    
        # setting the source and target nodes of the graph
        source = list(self.G.nodes())[0]
        target = list(self.G.nodes())[-1]

        # logging the source and target node ids
        logging.info(f'source: {source}')
        logging.info(f'target: {target}')
        
        shortest_path = nx.astar_path(self.G, source, target, heuristic=astar_heuristic(self.G), weight="length")

        astarStrategy = Astar()
        algo = algorithmSelection(astarStrategy)
            
        route = algo.compute_route(self.G, source, target, 0, False, 15)
        
        self.assertTrue(path_elevation(self.G, shortest_path) == route["net_elevation"], "Max elevation equal to shortest path")
        
    def test_DFS_With_Dijkstra_Max(self):
        logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s %(message)s') #setting up configurations
        logging.info('Running test_DFS_With_Dijkstra_Max')
    
        # setting the source and target nodes of the graph
        source = list(self.G.nodes())[0]
        target = list(self.G.nodes())[-1]

        # logging the source and target node ids
        logging.info(f'source: {source}')
        logging.info(f'target: {target}')
        
        shortest_path = nx.dijkstra_path(self.G, source, target, weight='length')

        astarStrategy = Dijkstra()
        algo = algorithmSelection(astarStrategy)
            
        route = algo.compute_route(self.G, source, target, 20, True, 15)
            
        self.assertTrue(path_elevation(self.G, shortest_path) <= route["net_elevation"], "Max elevation is greater than or equal to shortest path")
        
    def test_DFS_With_Dijkstra_Min(self):
        logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s %(message)s') #setting up configurations
        logging.info('Running test_DFS_With_Dijkstra_Min')
    
        # setting the source and target nodes of the graph
        source = list(self.G.nodes())[0]
        target = list(self.G.nodes())[-1]

        # logging the source and target node ids
        logging.info(f'source: {source}')
        logging.info(f'target: {target}')
        
        shortest_path = nx.dijkstra_path(self.G, source, target, weight='length')

        astarStrategy = Dijkstra()
        algo = algorithmSelection(astarStrategy)
            
        route = algo.compute_route(self.G, source, target, 20, False, 15)
        
        self.assertTrue(path_elevation(self.G, shortest_path) >= route["net_elevation"], "Max elevation is less than or equal to shortest path")
        
    def test_DFS_With_Dijkstra_Deviation_Zero(self):
        logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s %(message)s') #setting up configurations
        logging.info('Running test_DFS_With_Dijkstra_Deviation_Zero')
    
        # setting the source and target nodes of the graph
        source = list(self.G.nodes())[0]
        target = list(self.G.nodes())[-1]

        # logging the source and target node ids
        logging.info(f'source: {source}')
        logging.info(f'target: {target}')
        
        shortest_path = nx.dijkstra_path(self.G, source, target, weight='length')

        astarStrategy = Dijkstra()
        algo = algorithmSelection(astarStrategy)
            
        route = algo.compute_route(self.G, source, target, 0, False, 15)
        
        self.assertTrue(path_elevation(self.G, shortest_path) == route["net_elevation"], "Max elevation equal to shortest path")
        


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


from abc import ABC, abstractmethod
from .routeProcessing import simplify_graph, DFS, astar_heuristic
import networkx as nx

class RoutingAlgorithm(ABC):
    #routing interface
    
    @abstractmethod
    def shortestPath(graph, source, target, limit, isMax, cutoff):
        pass

class Dijkstra(RoutingAlgorithm):
    
    def shortestPath(graph, source, target, limit, isMax, cutoff):
            shortest_path = nx.dijkstra_path(graph, source, target, weight='length')
            shortest_path_length = nx.shortest_path_length(graph, source=source, target=target, weight='length')

            shortest_path_length_limit = ((limit/100) * shortest_path_length) + shortest_path_length

            visited = {node: False for node in graph.nodes}
            new_graph = simplify_graph(graph, shortest_path, cutoff)
            elevation_graph = DFS(shortest_path_length_limit, source, target, [], new_graph, visited, {})
            
            return isMax if (max(elevation_graph.items(), key=lambda x: x[0])[1]) else (min(elevation_graph.items(), key=lambda x: x[0])[1])
            
    
class Astar(RoutingAlgorithm):
    
    def shortestPath(graph, source, target, limit, isMax, cutoff):
            shortest_path = nx.astar_path(graph, source, target, heuristic=astar_heuristic(graph), weight="length")
            shortest_path_length = nx.astar_path_length(graph, source, target, heuristic=astar_heuristic(graph), weight="length")
            
            shortest_path_length_limit = ((limit/100) * shortest_path_length) + shortest_path_length
            visited = {node: False for node in graph.nodes}
            new_graph = simplify_graph(graph, shortest_path, cutoff)
            elevation_graph = DFS(shortest_path_length_limit, source, target, [], new_graph, visited, {})
            
            return isMax if (max(elevation_graph.items(), key=lambda x: x[0])[1]) else (min(elevation_graph.items(), key=lambda x: x[0])[1])
        

class algorithmSelection():
    
    def __init__(self, RoutingAlgorithm):
        self.RoutingAlgorithm = RoutingAlgorithm
        
    def compute_route(self, graph, source, target, limit, isMax, cutoff):
        return self.RoutingAlgorithm.shortestPath(graph, source, target, limit, isMax, cutoff)
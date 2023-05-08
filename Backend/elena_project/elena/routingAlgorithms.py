
from abc import ABC, abstractmethod
from .routeProcessing import astar_heuristic, simplify_graph, DFS
import networkx as nx

class RoutingAlgorithm(ABC):
    #routing interface
    
    @abstractmethod
    def shortestPath(graph, source, target, limit, isMax, cutoff):
        pass

class Dijkstra(RoutingAlgorithm):
    
    def shortestPath(self, graph, source, target, limit, isMax, cutoff):
            shortest_path = nx.dijkstra_path(graph, source, target, weight='length')
            shortest_path_length = nx.shortest_path_length(graph, source=source, target=target, weight='length')
            
            if limit == 0:
                return shortest_path

            shortest_path_length_limit = ((limit/100) * shortest_path_length) + shortest_path_length

            visited = {node: False for node in graph.nodes}
            new_graph = simplify_graph(graph, shortest_path, cutoff)
            elevation_graph = DFS(shortest_path_length_limit, source, target, [], new_graph, visited, {})
            
            route = max(elevation_graph.items(), key=lambda x: x[0])[1] if isMax else (min(elevation_graph.items(), key=lambda x: x[0])[1])
            
            routeCoord = []
            
            for nodeId in route:
                routeCoord.append(graph.nodes[nodeId])

            return routeCoord
            
    
class Astar(RoutingAlgorithm):
    
    def shortestPath(self, graph, source, target, limit, isMax, cutoff):
            shortest_path = nx.astar_path(graph, source, target, heuristic=astar_heuristic(graph), weight="length")
            shortest_path_length = nx.astar_path_length(graph, source, target, heuristic=astar_heuristic(graph), weight="length")
            
            if limit == 0:
                return shortest_path
            
            shortest_path_length_limit = ((limit/100) * shortest_path_length) + shortest_path_length
            
            visited = {node: False for node in graph.nodes}
            new_graph = simplify_graph(graph, shortest_path, cutoff)
            elevation_graph = DFS(shortest_path_length_limit, source, target, [], new_graph, visited, {})
            
            route = max(elevation_graph.items(), key=lambda x: x[0])[1] if isMax else (min(elevation_graph.items(), key=lambda x: x[0])[1])
            
            routeCoord = []
            
            for nodeId in route:
                routeCoord.append(graph.nodes[nodeId])

            return routeCoord
        

class algorithmSelection:
    
    def __init__(self, RoutingAlgorithm):
        self._RoutingAlgorithm = RoutingAlgorithm
        
    def compute_route(self, graph, source, target, limit, isMax, cutoff):
        return self._RoutingAlgorithm.shortestPath(graph, source, target, limit, isMax, cutoff)

from abc import ABC, abstractmethod
from .routeProcessing import astar_heuristic, simplify_graph, DFS, path_elevation, path_length
import networkx as nx

# define RoutingAlgorithm abstract base class
class RoutingAlgorithm(ABC):
    #routing interface
    
    @abstractmethod
    def shortestPath(graph, source, target, limit, isMax, cutoff):
        pass

# Dijkstra algorithm to find the optimal route
class Dijkstra(RoutingAlgorithm):
    
    # Use the networkx library's dijkstra algorithm to find the shortest path and its length
    def shortestPath(self, graph, source, target, limit, isMax, cutoff):
            shortest_path = nx.dijkstra_path(graph, source, target, weight='length')
            shortest_path_length = nx.shortest_path_length(graph, source=source, target=target, weight='length')
            
            if limit == 0:
                routeCoord = []
            
                for nodeId in shortest_path:
                    routeCoord.append(graph.nodes[nodeId])
                    
                return { 'route_length': path_length(graph, shortest_path), 'net_elevation': path_elevation(graph, shortest_path), 'path': routeCoord }
            
            # calculate route based on the percentage limit given
            shortest_path_length_limit = ((limit/100) * shortest_path_length) + shortest_path_length

            # cutoff for the dfs
            cutoffs = ((len(shortest_path) * (limit/100))) + len(shortest_path)
            
            # new_graph = simplify_graph(graph, shortest_path, cutoff)
            new_graph = graph

            # use depth-first search to explore elevation changes within the length limit
            elevation_graph = DFS(shortest_path_length_limit, source, target, [], new_graph, {}, cutoffs, 0, not isMax)

            # number of different paths
            print(len(elevation_graph))
            
            if len(elevation_graph) == 0:
                route = shortest_path
            else:
                # select the optimal route based on whether we want to maximize or minimize the elevation changes
                route = elevation_graph['path']
            
            routeCoord = []
            
            for nodeId in route:
                routeCoord.append(graph.nodes[nodeId])
                
            elevation_net_change = path_elevation(new_graph, route);
            
            length_of_path = path_length(new_graph, route);

            return { 'route_length': length_of_path, 'net_elevation': elevation_net_change, 'path': routeCoord };
            

# A* algorithm to find the optimal route
class Astar(RoutingAlgorithm):
    
    def shortestPath(self, graph, source, target, limit, isMax, cutoff):
            # use the networkx library's A* algorithm to find the shortest path and its length
            shortest_path = nx.astar_path(graph, source, target, heuristic=astar_heuristic(graph), weight="length")
            shortest_path_length = nx.astar_path_length(graph, source, target, heuristic=astar_heuristic(graph), weight="length")

            if limit == 0:
                routeCoord = []
            
                for nodeId in shortest_path:
                    routeCoord.append(graph.nodes[nodeId])
                    
                return { 'route_length': path_length(graph, shortest_path), 'net_elevation': path_elevation(graph, shortest_path), 'path': routeCoord }
            
            # calculate route based on the percentage limit given
            shortest_path_length_limit = ((limit/100) * shortest_path_length) + shortest_path_length
            
            # cutoff for the dfs
            cutoffs = ((len(shortest_path) * (limit/100))) + len(shortest_path)
            
            # new_graph = simplify_graph(graph, shortest_path, cutoff)
            new_graph = graph

            # use depth-first search to explore elevation changes within the length limit
            elevation_graph = DFS(shortest_path_length_limit, source, target, [], new_graph, {}, cutoffs, 0, not isMax)

            # number of different paths
            print(len(elevation_graph))
            
            if len(elevation_graph) == 0:
                route = shortest_path
            else:
                # select the optimal route based on whether we want to maximize or minimize the elevation changes
                route = elevation_graph['path']
                
            routeCoord = []
            print(route)
            for nodeId in route:
                routeCoord.append(graph.nodes[nodeId])

            elevation_net_change = path_elevation(new_graph, route);
            
            length_of_path = path_length(new_graph, route);
            
            print("here")

            return { 'route_length': length_of_path, 'net_elevation': elevation_net_change, 'path': routeCoord };
        

class algorithmSelection:
    
    def __init__(self, RoutingAlgorithm):
        self._RoutingAlgorithm = RoutingAlgorithm
        
    # this method computes the shortest path using the selected algorithm
    # input parameters:
    #   graph: the input graph for finding the shortest path
    #   source: the source node from where the path starts
    #   target: the destination node to which the path leads
    #   limit: the limit provied
    #   isMax: boolean variable indicating whether the elevation changes should be maximized or minimized
    #   cutoff: threshold distance to simplify the graph during path computation
    # output:
    #   returns a list of nodes in the computed shortest path
    def compute_route(self, graph, source, target, limit, isMax, cutoff):
        return self._RoutingAlgorithm.shortestPath(graph, source, target, limit, isMax, cutoff)
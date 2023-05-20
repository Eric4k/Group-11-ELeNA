# from .geoDataRetriever import getBikingData, getDrivingData, getWalkingData, loadGraphMLData
import networkx as nx
import osmnx as ox
import sys
from collections import deque
import heapq
# from .routingAlgorithms import Astar, algorithmSelection
print('test')

# geoDataGraphWalk = ox.load_graphml("dataSets/Amherst_Walk_Data.graphml")

sys.setrecursionlimit(5000)
def astar_heuristic(graph):
        return lambda nodeA, nodeB: nx.dijkstra_path_length(graph, nodeA, nodeB, weight="length")
    
# get the elevation of a path
def path_elevation(G, path):
    elevation = 0
    for i in range(len(path)-1):
        elevation += (G.nodes[path[i]]['elevation'] - G.nodes[path[i+1]]['elevation']) if (G.nodes[path[i]]['elevation'] - G.nodes[path[i+1]]['elevation']) > 0 else 0
    return elevation

# get the length of a path
def path_length(G, path):
    length = 0
    for i in range(len(path)-1):
        if '0' in G[path[i]][path[i+1]]: 
            length += G[path[i]][path[i+1]]['0']['length'] 
        else: 
            length += G[path[i]][path[i+1]][0]['length']
    return length

# simplify the graph, only add edges/nodes that connect nodes in the shortest path
def simplify_graph(G, shortest_path, cutoff):
    new_graph = nx.DiGraph()

    graphNodes = []
    
    # add edges that connect nodes in the shortest path
    for i in range(len(shortest_path)-1):
        current_node = shortest_path[i]
        next_node = shortest_path[i+1]
        for simple_path in nx.all_simple_paths(G, source=current_node, target=next_node, cutoff=cutoff): #maybe make cutoff a variable
            for j in range(len(simple_path)-1):
                edge_data = G[simple_path[j]][simple_path[j+1]]
                
                if simple_path[j] not in graphNodes:
                    new_graph.add_node(simple_path[j], **G.nodes[simple_path[j]])
                    graphNodes.append(simple_path[j])
                
                if simple_path[j+1] not in graphNodes:
                    new_graph.add_node(simple_path[j+1], **G.nodes[simple_path[j+1]])
                    graphNodes.append(simple_path[j+1])
                
                new_graph.add_edge(simple_path[j], simple_path[j+1], **{str(k): v for k, v in edge_data.items()})
    return new_graph

# DFS to find the path with the max elevation and is within the limit
def DFS_OLD(limit, source, target, path, graph, best_path, cutoff, index):
    try:
        if limit >= 0 and index <= cutoff:
            path.append(source)
            if source == target:
                best_path[path_elevation(graph, path)] = path.copy()
                # print("FOUND: ", path_elevation(graph, path), path_length(graph, path))
            else:
                for neighbor in graph.successors(source):
                    edge_data = graph.get_edge_data(source, neighbor)
 
                    if '0' in edge_data: 
                        edge_length = edge_data['0']['length'] 
                    else: 
                        edge_length = edge_data[0]['length']
                
                    if neighbor not in path:
                        DFS_OLD(limit - edge_length, neighbor, target, path, graph, best_path, cutoff, index + 1)

            path.pop()
        return best_path 
    except Exception as e:
        print(e)

def DFS(limit, source, target, path, graph, best_path, cutoff, index):
    try:
        if limit >= 0 and index <= cutoff:
            path.append(source)
            if source == target:
                elevation = path_elevation(graph, path)
                if 'elevation' not in best_path or elevation > best_path['elevation']:
                    best_path['elevation'] = elevation
                    best_path['path'] = path.copy()
            else:
                for neighbor in graph.successors(source):
                    edge_data = graph.get_edge_data(source, neighbor)

                    if '0' in edge_data:
                        edge_length = edge_data['0']['length']
                    else:
                        edge_length = edge_data[0]['length']

                    if neighbor not in path:
                        new_limit = limit - edge_length
                        # Prune if the maximum elevation gain is less than or equal to the current best. UPDATE: best_path length now taken into account
                        if 'elevation' in best_path:
                            len_diff = abs(len(path + [neighbor]) - len(best_path['path']))
                            bpe = best_path['path'][:-len_diff]
                            # print("BPE: ", bpe, best_path['path'])
                            if path_elevation(graph, path + [neighbor]) <= path_elevation(graph, bpe):#best_path['elevation']:
                                continue

                        DFS(new_limit, neighbor, target, path, graph, best_path, cutoff, index + 1)

            path.pop()
        return best_path
    except Exception as e:
        print(e)
#small test
# source = 64056128
# target = 9057663144

# shortest_path = nx.dijkstra_path(geoDataGraphWalk, source, target, weight='length')
# shortest_path_length = nx.shortest_path_length(geoDataGraphWalk, source=source, target=target, weight='length')

# limit = 90
# shortest_path_length_limit = ((limit/100) * shortest_path_length) + shortest_path_length

# visited = {node: False for node in geoDataGraphWalk.nodes}
# new_graph = simplify_graph(geoDataGraphWalk, shortest_path)
# max_elevation = DFS(shortest_path_length_limit, source, target, [], new_graph, visited, {})

# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("SHORTEST PATH: " + str(shortest_path))
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# best_max_elevation = max(max_elevation.items(), key=lambda x: x[0])[1]
# best_min_elevation = min(max_elevation.items(), key=lambda x: x[0])[1]

# # print(max(max_elevation.items(), key=lambda x: x[0]), shortest_path_length, shortest_path_length_limit)
# new_graph = simplify_graph(geoDataGraphWalk, shortest_path, 20)
# max_elevation = DFS(shortest_path_length_limit, source, target, [], new_graph, visited, {})

# best_max_elevation = max(max_elevation.items(), key=lambda x: x[0])[1]
# best_min_elevation = min(max_elevation.items(), key=lambda x: x[0])[1]

# print(max(max_elevation.items(), key=lambda x: x[0]), shortest_path_length, shortest_path_length_limit)
# route = ox.plot_route_folium(geoDataGraphWalk, best_max_elevation, popup_attribute="name", route_color='green', route_width=3)
# route.save("map2.html")

# route = ox.plot_route_folium(geoDataGraphWalk, best_min_elevation, popup_attribute="name", route_color='green', route_width=3)
# route.save("map3.html")

# dp1 = nx.dijkstra_path(geoDataGraphWalk, source, target, weight="length")
# route = ox.plot_route_folium(geoDataGraphWalk, dp1, popup_attribute="name", route_color='green', route_width=3)
# route.save("map1.html")

#test astar
# def test_astar(geoDataGraphWalk):

#     source = 64056128
#     target = 9057663144
    # astar_shortest_path = nx.astar_path(geoDataGraphWalk, source, target, heuristic=astar_heuristic(geoDataGraphWalk), weight="length")
    # astar_shortest_path_length = nx.astar_path_length(geoDataGraphWalk, source, target, heuristic=astar_heuristic(geoDataGraphWalk), weight="length")

    # limit = 90
    # astar_shortest_path_length_limit = ((limit/100) * astar_shortest_path_length) + astar_shortest_path_length
    # visited = {node: False for node in geoDataGraphWalk.nodes}
    # new_graph = simplify_graph(geoDataGraphWalk, astar_shortest_path, 30)
    # graph_elevation = DFS(astar_shortest_path_length_limit, source, target, [], new_graph, visited, {})

    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("SHORTEST PATH: " + str(astar_shortest_path))
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # best_max_elevation = max(graph_elevation.items(), key=lambda x: x[0])[1]
    # best_min_elevation = min(graph_elevation.items(), key=lambda x: x[0])[1]
    
    # astar = Astar()
    
    # routing = algorithmSelection(astar)
    
    # path = routing.compute_route(geoDataGraphWalk, source, target, 80, True, 20)
    
    # print(path)
    

    # print(max(max_elevation.items(), key=lambda x: x[0]), shortest_path_length, shortest_path_length_limit)
    # route = ox.plot_route_folium(geoDataGraphWalk, best_max_elevation, popup_attribute="name", route_color='green', route_width=3)
    # route.save("map2.html")

    # route = ox.plot_route_folium(geoDataGraphWalk, best_min_elevation, popup_attribute="name", route_color='green', route_width=3)
    # route.save("map3.html")

    # dp1 = nx.astar_path(geoDataGraphWalk, source, target, heuristic=astar_heuristic(geoDataGraphWalk), weight="length")
    # route = ox.plot_route_folium(geoDataGraphWalk, dp1, popup_attribute="name", route_color='green', route_width=3)
    # route.save("map1.html")
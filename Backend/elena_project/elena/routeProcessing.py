# from geoDataRetriever import geoDataGraphBike, geoDataGraphDrive, geoDataGraphWalk
import networkx as nx
import osmnx as ox

geoDataGraphWalk = ox.load_graphml("dataSets/Amherst_Bike_Data.graphml")

def path_elevation(G, path):
    elevation = 0
    for i in range(len(path)-1):
        elevation += abs(G.nodes[path[i]]['elevation'] - G.nodes[path[i+1]]['elevation'])
    return elevation

def path_length(G, path):
    length = 0
    for i in range(len(path)-1):
        length += G[path[i]][path[i+1]]['0']['length']
    return length

def simplify_graph(G, shortest_path):
    new_graph = nx.Graph()
    for node in G.nodes:
        new_graph.add_node(node, **G.nodes[node])

    for i in range(len(shortest_path)-1):
        current_node = shortest_path[i]
        next_node = shortest_path[i+1]
        for simple_path in nx.all_simple_paths(G, source=current_node, target=next_node, cutoff=20):
            for j in range(len(simple_path)-1):
                edge_data = G[simple_path[j]][simple_path[j+1]]
                new_graph.add_edge(simple_path[j], simple_path[j+1], **{str(k): v for k, v in edge_data.items()})
    return new_graph

def DFS(limit, source, target, path, graph, visited, best_path):
    visited[source] = True
    if limit >= 0:
        path.append(source)
        if source == target:
            best_path[path_elevation(graph, path)] = path.copy()
            print("FOUND: ", path_elevation(graph, path), path_length(graph, path))
        else:
            for neighbor in nx.all_neighbors(graph, source):
                edge_data = graph.get_edge_data(source, neighbor)
                edge_length = edge_data['0']['length']

                if visited[neighbor] == False:
                        DFS(limit - edge_length, neighbor, target, path, graph, visited, best_path)

        path.pop()
        visited[source] = False
    return best_path    


#small test
source = 64056128
target = 9057663144
shortest_path = nx.dijkstra_path(geoDataGraphWalk, source, target, weight='length')
shortest_path_length = nx.shortest_path_length(geoDataGraphWalk, source=source, target=target, weight='length')
limit = 90/100 
shortest_path_length_limit = (limit * shortest_path_length) + shortest_path_length

visited = {node: False for node in geoDataGraphWalk.nodes}

new_graph = simplify_graph(geoDataGraphWalk, shortest_path)
max_elevation = DFS(shortest_path_length_limit, source, target, [], new_graph, visited, {})

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("SHORTEST PATH: " + str(shortest_path))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

best_max_elevation = max(max_elevation.items(), key=lambda x: x[0])[1]
print("DA MKIS: ", max(max_elevation.items(), key=lambda x: x[0]), shortest_path_length, shortest_path_length_limit)
route = ox.plot_route_folium(geoDataGraphWalk, best_max_elevation, popup_attribute="name", route_color='green', route_width=3)
route.save("map2.html")

dp1 = nx.dijkstra_path(geoDataGraphWalk, source, target, weight="length")
route = ox.plot_route_folium(geoDataGraphWalk, dp1, popup_attribute="name", route_color='green', route_width=3)
route.save("map1.html")


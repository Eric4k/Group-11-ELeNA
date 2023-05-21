import networkx as nx

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

# DFS to find the path with the max elevation and is within the limit and returns multiple paths if found
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

# find the maximum or minimum elevation path within the limit of the deviation
def DFS(limit, source, target, path, graph, best_path, cutoff, index, min_elevation):
    try:
        if limit >= 0 and index <= cutoff:
            path.append(source)
            if source == target:
                elevation = path_elevation(graph, path)

                if min_elevation:
                    if 'elevation' not in best_path or elevation < best_path['elevation']:
                        best_path['elevation'] = elevation
                        best_path['path'] = path.copy()
                else:
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
                        # Prune if the maximum/minimum elevation gain is less than or equal to the current best. UPDATE: best_path length now taken into account
                        if 'elevation' in best_path:
                            len_diff = abs(len(path + [neighbor]) - len(best_path['path']))
                            bpe = best_path['path'][:-len_diff]
                            # print("BPE: ", bpe, best_path['path'])
                            if min_elevation:
                                if path_elevation(graph, path + [neighbor]) >= path_elevation(graph, bpe):#best_path['elevation']:
                                    continue
                            else: 
                                if path_elevation(graph, path + [neighbor]) <= path_elevation(graph, bpe):#best_path['elevation']:
                                    continue

                        DFS(new_limit, neighbor, target, path, graph, best_path, cutoff, index + 1, min_elevation)

            path.pop()
        return best_path
    except Exception as e:
        print(e)
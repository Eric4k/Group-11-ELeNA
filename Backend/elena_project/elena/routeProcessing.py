# from geoDataRetriever import geoDataGraphBike, geoDataGraphDrive, geoDataGraphWalk
import networkx as nx
import osmnx as ox

geoDataGraphWalk = ox.load_graphml("dataSets/Amherst_Walk_Data.graphml")
print(geoDataGraphWalk)



source = 66590880
target = 66603815

shortest_path_length = nx.shortest_path_length(G, source=source, target=target, weight='length')
print(dp)

route = ox.plot_route_folium(geoDataGraphWalk, dp, popup_attribute="name", route_color='green', route_width=3)
route.save("map.html")
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import osmnx as ox
import requests
from .routingAlgorithms import algorithmSelection, Astar, Dijkstra
from .geoDataRetriever import getBikingData, getWalkingData, initializeGeoDataGraphs, loadGraphMLData
from pathlib import Path



# Create your views here.
@api_view(["GET"])
def getRoute(request):
    try:
        #get the source and and destination needed to calculate the longitude and latitude
        start = request.GET.get('source', None);
        end = request.GET.get('destination', None);
       
        if start == None or end == None:
            return Response({"status:" "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
        origin_point = ox.geocoder.geocode(start);
        destination_point = ox.geocoder.geocode(end);

        #get the mode of transportation from the request parameters
        modeOfTransport = request.GET.get('modeOfTransport', 'walk') #walk is the default mode

        #get the user's elevation preference from the request parameters
        elev_preference = request.GET.get('elev_preference', 'min') #min is the default choice
        
        #percentage deviation from shortest path
        percentage_deviation = float(request.GET.get('deviation', 0));
        
        #algorithm selection, default to dijkstra
        algorithm = request.GET.get('algorithm', 'dijkstra')

        graph = None
        elevation = True if elev_preference == 'max' else False
        #TODO
        cutoff = 50
        
        if modeOfTransport == 'walk':
            graph = getWalkingData()
        else:
            graph = getBikingData()


        #call function in route processing to process the data then pass it to route processing
        source = ox.nearest_nodes(graph, origin_point[1], origin_point[0], False)
        target = ox.nearest_nodes(graph, destination_point[1], destination_point[0], False)
        
        #nearest node could return a list
        if type(source) is list:
            source = source[0]
            target = target[0]
        
  
        if algorithm == 'dijkstra':
            dijkstraStrategy = Dijkstra()
            algo = algorithmSelection(dijkstraStrategy)
            
            route = algo.compute_route(graph, source, target, percentage_deviation, elevation, cutoff)
            
            return Response({'route_detail': route}, status=status.HTTP_200_OK)
        else:
            astarStrategy = Astar()
            algo = algorithmSelection(astarStrategy)
            
            route = algo.compute_route(graph, source, target, percentage_deviation, elevation, cutoff)
            
            return Response({'route_detail': route}, status=status.HTTP_200_OK)

    except:
        return Response({"status:" "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
    
# Create your views here.
@api_view(["POST"])
def changeCity(request):
    jsonBody = request.POST.copy()
    city = jsonBody['city']
    state = jsonBody['state']
    
    city_walk_graph_exist = Path(f"dataSets/{city}_{state}_Walk.graphml")
    city_bike_graph_exist = Path(f"dataSets/{city}_{state}_Bike.graphml")
    
    if city_walk_graph_exist.is_file() and city_bike_graph_exist.is_file():
        loadGraphMLData(city, state)
    else:
        initializeGeoDataGraphs(city, state)
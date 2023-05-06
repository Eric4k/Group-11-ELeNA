from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import osmnx as ox
import requests
from .routingAlgorithms import algorithmSelection, Astar, Dijkstra
from .geoDataRetriever import getBikingData, getDrivingData, getWalkingData


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
        percentage_deviation = request.GET.get('deviation', 0);
        
        #algorithm selection, default to dijkstra
        algorithm = request.GET.get('algorithm', 'dijkstra')
        
        path = None
        graph = None
        elevation = elev_preference == 'min' if True else False\
        #TODO
        cutoff = 30
        
        if modeOfTransport == 'walk':
            graph = getWalkingData()
        elif modeOfTransport == 'bike':
            graph = getBikingData()
        else:
            graph = getDrivingData()

        #call function in route processing to process the data then pass it to route processing
        
        if algorithm == 'dijkstra':
            dijkstraStrategy = Dijkstra(graph, origin_point, destination_point, percentage_deviation, elevation, cutoff)
            path = algorithmSelection(dijkstraStrategy)
        else:
            astarStrategy = Astar(graph, origin_point, destination_point, percentage_deviation, elevation, cutoff)
            path = algorithmSelection(astarStrategy)

        # Build response
        response_data = {
            'route': 'route',
            'elevations': 'elevations'
        }

    except:
        return Response({"status:" "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
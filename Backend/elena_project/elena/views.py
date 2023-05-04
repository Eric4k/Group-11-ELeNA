from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import osmnx as ox
import requests


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

        #get the key value pair or set the value to none
        startLongitude = origin_point[0];
        startLatitude = origin_point[1];
        endLongitude = destination_point[0];
        endLatitude = destination_point[1];

        #get the mode of transportation from the request parameters
        modeOfTransport = request.GET.get('modeOfTransport', 'walk') #walk is the default mode

        #get the user's elevation preference from the request parameters
        elev_preference = request.GET.get('elev_preference', 'min') #min is the default choice
        
        #percentage deviation from shortest path
        percentage_deviation = request.GET.get('deviation', 0);
        

        #call function in route processing to process the data then pass it to route processing

        # Call OSMnx to get the nearest edges between the points

        G = ox.graph_from_point(origin_point, distance=1000, network_type=modeOfTransport)
        start_node = ox.get_nearest_node(G, origin_point)
        end_node = ox.get_nearest_node(G, destination_point)

        route = ''
        # if elev_preference == 'min':
        #     do something here to get route
        # elif elev_preference == 'max':
        #     do something here to get route


        elevations = []
        #do elevation calculation here

        # Build response
        response_data = {
            'route': route,
            'elevations': elevations
        }

    except:
        return Response({"status:" "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
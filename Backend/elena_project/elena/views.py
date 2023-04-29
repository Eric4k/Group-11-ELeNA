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
        #get the key value pair or set the value to none
        startLongitude = request.GET.get('startLong', None)
        startLatitude = request.GET.get('startLat', None)
        endLongitude = request.GET.get('endLong', None)
        endLatitude = request.GET.get('endLat', None)

        #get the mode of transportation from the request parameters
        modeOfTransport = request.GET.get('modeOfTransport', 'walk') #walk is the default mode

        #get the user's elevation preference from the request parameters
        elev_preference = request.GET.get('elev_preference', 'min') #min is the default choice

        # Call OSMnx to get the nearest edges between the points
        start_point = (float(startLatitude), float(startLongitude))
        end_point = (float(endLatitude), float(endLongitude))
        G = ox.graph_from_point(start_point, distance=1000, network_type=modeOfTransport)
        start_node = ox.get_nearest_node(G, start_point)
        end_node = ox.get_nearest_node(G, end_point)

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


        if startLongitude == None or startLatitude == None or endLongitude == None or endLatitude == None:
            return Response({"status:" "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
        else:  
            #call function in route processing to process the data then pass it to route processing
            return Response({"success"})
    except:
        return Response({"status:" "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
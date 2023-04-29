from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def getRoute(request):
    try:
        #get the key value pair or set the value to none
        startLongitude = request.GET.get('startLong', None)
        startLatitude = request.GET.get('startLat', None)
        endLongitude = request.GET.get('endLong', None)
        endLatitude = request.GET.get('endLat', None)
        if startLongitude == None or startLatitude == None or endLongitude == None or endLatitude == None:
            return Response({"status:" "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
        else:  
            #call function in route processing to process the data then pass it to route processing
            return Response({"success"})
    except:
        return Response({"status:" "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
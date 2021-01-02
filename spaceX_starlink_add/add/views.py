from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Satellite
from .serializers import SatelliteSerializer

"""

"""


@api_view(['GET', 'POST'])
def satellite_add_list(request, format=None):
    if request.method == 'GET':  # user requesting data
        snippets = Satellite.objects.all()
        serializer = SatelliteSerializer(snippets, many=True)
        return Response(serializer.data,
                        headers={
                            'Access-Control-Allow-Credentials': True,
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': 'GET',
                            'Access-Control-Allow-Headers': 'application/json',
                        }
                        )

    elif request.method == 'POST':  # user posting data
        serializer = SatelliteSerializer(data=request.data)

        try:
            obj = Satellite.objects.get(pk=request.data["satelliteId"])
            if "healthPercentage" in request.data:
                obj.healthPercentage = request.data["healthPercentage"]
            if "xVelocity" in request.data:
                obj.xVelocity = request.data["xVelocity"]
            if "yVelocity" in request.data:
                obj.yVelocity = request.data["yVelocity"]
            if "xCoordinate" in request.data:
                obj.xCoordinate = request.data["xCoordinate"]
            if "yCoordinate" in request.data:
                obj.yCoordinate = request.data["yCoordinate"]
            obj.save()
            return Response(status=status.HTTP_202_ACCEPTED)

        except:
            if serializer.is_valid():
                serializer.save()  # save to db
                # Sending data to healthCheck micro service
                # requests.post("http://127.0.0.1:8002/healthCheck/", data=request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def satellite_add_details(request, pk, format=None):
    try:
        snippet = Satellite.objects.get(pk=pk)
    except Satellite.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SatelliteSerializer(snippet)
        return Response(serializer.data,
                        headers={
                            'Access-Control-Allow-Credentials': True,
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': 'GET',
                            'Access-Control-Allow-Headers': 'application/json',
                        }
                        )

    elif request.method == 'PUT':
        serializer = SatelliteSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import serializers
from .models import Satellite


class SatelliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Satellite
        fields = ('satelliteId', 'satelliteName', 'comments', 'xCoordinate', 'yCoordinate',
                  'xVelocity', 'yVelocity', 'added_on', 'healthPercentage')

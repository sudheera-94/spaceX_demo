from django.db import models


class Satellite(models.Model):
    satelliteId = models.IntegerField(primary_key=True)
    satelliteName = models.CharField(max_length=20, blank=True)
    comments = models.CharField(max_length=100, blank=True)
    healthPercentage = models.IntegerField(default=100, blank=True)
    added_on = models.DateTimeField(auto_now_add=True, blank=True)
    xCoordinate = models.IntegerField(blank=True)
    yCoordinate = models.IntegerField(blank=True)
    xVelocity = models.IntegerField(default=0, blank=True)
    yVelocity = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.satelliteName

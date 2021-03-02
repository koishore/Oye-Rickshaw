from django.db import models

from geopy.distance import distance as D


class Rickshaw(models.Model):
    type = models.CharField(max_length=30)
    license = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    lat = models.FloatField()
    long = models.FloatField()

    def __str__(self):
        return "{}_{}".format(self.name, self.license)
        
    def is_nearby(self, lati, longi):
        return D((self.lat,self.long),(lati,longi))._Distance__kilometers <= 0.2

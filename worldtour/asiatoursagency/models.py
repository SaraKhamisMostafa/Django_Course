from django.db import models

# Create your models here.
class Tour(models.Model):
    #we nees a origin country ,we need adstination , 
    #nuber of nights, and we need the price for that tour.
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()
    #this is a stringe representation for the tour
    def __str__(self):
        return (f"ID:{self.id}:From {self.origin_country} To {self.destination_country},{self.number_of_nights} nights costs ${self.price}")

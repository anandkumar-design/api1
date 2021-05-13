from django.db import models

class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operationAirlines = models.CharField(max_length=20)
    depatureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateOfDepature = models.DateField()
    estimatedTimeOfDepature = models.TimeField()

class Passenger(models.Model):
    FirstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    MiddleName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)

class Reservation(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger,on_delete=models.CASCADE)




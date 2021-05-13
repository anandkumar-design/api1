from rest_framework import serializers
from.models import Flight,Passenger,Reservation
import re

def isFlightNumberValid(data):
    print("isFlightNumberValid")


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators=[isFlightNumberValid]

    def validate_flightNumber(self,flightNumber):
        print("validate_flightNumber")
        if(re.match("^[a-zA-z0-9]*$",flightNumber)==None):
            raise serializers.ValidationError("Invalid Flight Number")
        return flightNumber

    def validate(self,data):
        print("validate")
        print(data["flightNumber"])
        return data

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
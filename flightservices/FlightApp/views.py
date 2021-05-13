from django.shortcuts import render
from.models import Flight,Passenger,Reservation
from.serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['POST'])
def Find_flights(request):
    flights = Flight.objects.filter(depatureCity=request.data['depatureCity'],arrivalCity=request.datat['arrivalCity'])
    serializer=FlightSerializer(flights,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_reservation():
   flight = Flight.objects.get(id=request.data['flightId'])

   passenger = Passenger()
   passenger.firstName = request.data['firstName']
   passenger.lastName = request.data['lastName']
   passenger.MiddleName = request.data['MiddleName']
   passenger.email = request.data['email']
   passenger.phone = request.data['phone']
   passenger.save()

   reservation = Reservation()
   reservation.flight = flight
   reservation.passenger = passenger

   reservation.save()
   return Response(status = status.HTTP_201_CREATED) 


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

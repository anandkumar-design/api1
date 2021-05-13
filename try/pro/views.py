from django.shortcuts import render
from django.http import JsonResponse
from.models import emp
from .serializers import empserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes


@api_view(('GET',))
def index(request):
    if request.method == 'GET':
        sub = emp.objects.all()
        serializer = empserializers(sub,many=True)
        return Response(serializer.data)

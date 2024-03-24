from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from territory.models import TerritorialUnits, Location
from territory.serializers import TerritorialUnitsSerializer, LocationSerializer


class TerritorialUnitsListView(generics.ListAPIView):
    queryset = TerritorialUnits.objects.all()
    serializer_class = TerritorialUnitsSerializer
    permission_classes = (AllowAny, )


class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (AllowAny, )

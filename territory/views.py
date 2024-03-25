from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from territory.models import TerritorialUnit, Location
from territory.serializers import TerritorialUnitSerializer, LocationSerializer


class TerritorialUnitListView(generics.ListAPIView):
    queryset = TerritorialUnit.objects.all()
    serializer_class = TerritorialUnitSerializer
    permission_classes = (AllowAny, )


class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (AllowAny, )

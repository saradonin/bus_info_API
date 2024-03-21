from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from territory.models import TerritorialUnits
from territory.serializers import TerritorialUnitsSerializer


class TerritorialUnitsListView(generics.ListAPIView):
    queryset = TerritorialUnits.objects.all()
    serializer_class = TerritorialUnitsSerializer
    permission_classes = (AllowAny, )
    

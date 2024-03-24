from rest_framework import serializers
from territory.models import TerritorialUnits, Location


class TerritorialUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerritorialUnits
        fields = '__all__'


class LocationSerializer(serializers.Serializer):
    class Meta:
        model = Location
        fields = '__all__'

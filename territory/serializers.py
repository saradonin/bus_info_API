from rest_framework import serializers
from territory.models import TerritorialUnit, Location


class TerritorialUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerritorialUnit
        fields = '__all__'


class LocationSerializer(serializers.Serializer):
    class Meta:
        model = Location
        fields = '__all__'

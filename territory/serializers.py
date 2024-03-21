from rest_framework import serializers
from territory.models import TerritorialUnits


class TerritorialUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerritorialUnits
        fields = '__all__'

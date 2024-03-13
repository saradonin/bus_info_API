from rest_framework import serializers
from bus_lines.models import Organizer, Carrier, Line


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = '__all__'


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = '__all__'


class LineSerializer(serializers.ModelSerializer):
    carrier = serializers.SlugRelatedField(
        queryset=Carrier.objects.all(), slug_field='id')
    organizer = serializers.SlugRelatedField(
        queryset=Organizer.objects.all(), slug_field='id')

    class Meta:
        model = Line
        fields = '__all__'

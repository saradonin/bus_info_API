from rest_framework import generics
from bus_lines.models import Carrier, Organizer, Line
from bus_lines.serializers import CarrierSerializer, OrganizerSerializer, LineSerializer


class OrganizerListView(generics.ListCreateAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer



class CarrierListView(generics.ListCreateAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer
    
    
class LineListView(generics.ListCreateAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer
from rest_framework import generics
from bus_lines.models import Organizer
from bus_lines.serializers import OrganizerSerializer


class OrganizerListView(generics.ListCreateAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer


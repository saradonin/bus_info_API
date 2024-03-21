from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from bus_lines.models import Carrier, Organizer, Line
from bus_lines.serializers import CarrierSerializer, OrganizerSerializer, LineSerializer


class OrganizerListCreateView(generics.ListCreateAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class OrganizerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
    permission_classes = (IsAuthenticated, )


class CarrierListCreateView(generics.ListCreateAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CarrierRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class LineListCreateView(generics.ListCreateAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class LineListByOrganizerView(generics.ListCreateAPIView):
    serializer_class = LineSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        organizer_id = self.kwargs['organizer_id']
        return Line.objects.filter(organizer_id=organizer_id)


class LineListByCarrierView(generics.ListCreateAPIView):
    serializer_class = LineSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        carrier_id = self.kwargs['carrier_id']
        return Line.objects.filter(carrier_id=carrier_id)


class LineRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

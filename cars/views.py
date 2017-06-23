from django.db.models import Count
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CarSerializer, EjectorCountSerializer, FuelRatingSerializer
from .models import Car
from .filters import EjectorCountFilterSet, FuelEfficiencyFilterSet


class CreateCarAPIView(viewsets.ModelViewSet):
    serializer_class = CarSerializer


class EjectorCountAPIView(viewsets.ModelViewSet):
    serializer_class = EjectorCountSerializer
    queryset = Car.objects.all()
    filter_class = EjectorCountFilterSet

    def get_queryset(self):
        return self.filter_queryset(super().get_queryset())\
            .filter(has_ejector_seat=True)\
            .aggregate(count=Count('pk'))

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset())
        return Response(serializer.data)


class FuelRatingAPIView(viewsets.ModelViewSet):
    serializer_class = FuelRatingSerializer
    queryset = Car.objects.all()
    filter_class = FuelEfficiencyFilterSet

    def get_queryset(self):
        return self.filter_queryset(super().get_queryset()) \
            .values('fuel_efficiency_rating')\
            .annotate(count=Count('fuel_efficiency_rating'))\
            .order_by('-count')\
            .first()

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset())
        return Response(serializer.data)

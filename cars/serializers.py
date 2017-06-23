from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class EjectorCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()


class FuelRatingSerializer(serializers.Serializer):
    fuel_efficiency_rating = serializers.CharField()

import django_filters
from .models import Car


class EjectorCountFilterSet(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = ['colour']


class FuelEfficiencyFilterSet(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(name="price", lookup_expr='gte')

    class Meta:
        model = Car
        fields = ['min_price', 'make']

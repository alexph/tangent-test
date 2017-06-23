from django.utils import timezone
import factory
from .models import Car


class CarFactory(factory.DjangoModelFactory):
    make = factory.Iterator(Car.MAKES)
    manufacture_date = factory.LazyFunction(timezone.now)
    colour = factory.Iterator(Car.COLOURS)
    sale_price = 999.99
    fuel_efficiency_rating = factory.Iterator(Car.FUEL_EFFICIENCY)
    has_ejector_seat = False

    class Meta:
        model = Car

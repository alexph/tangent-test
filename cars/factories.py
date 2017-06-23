from django.utils import timezone
import factory
from .models import Car


class CarFactory(factory.DjangoModelFactory):
    make = factory.Iterator(dict(Car.MAKES).values())
    manufacture_date = factory.LazyFunction(timezone.now)
    colour = factory.Iterator(dict(Car.COLOURS).values())
    sale_price = 999.99
    fuel_efficiency_rating = factory.Iterator(dict(Car.FUEL_EFFICIENCY).values())
    has_ejector_seat = False

    class Meta:
        model = Car

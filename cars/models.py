from django.db import models


class Car(models.Model):
    MAKE_VOLVO = 'Volvo'
    MAKE_BMW = 'BMW'
    MAKE_FORD = 'Ford'
    MAKE_MERCEDES = 'Mercedes'
    MAKE_ASTON_MARTIN = 'Aston Martin'

    MAKES = [
        (MAKE_VOLVO, MAKE_VOLVO),
        (MAKE_BMW, MAKE_BMW),
        (MAKE_FORD, MAKE_FORD),
        (MAKE_MERCEDES, MAKE_MERCEDES),
        (MAKE_ASTON_MARTIN, MAKE_ASTON_MARTIN),
    ]

    COLOUR_RED = 'red'
    COLOUR_BLUE = 'blue'
    COLOUR_GREEN = 'green'
    COLOUR_ORANGE = 'orange'
    COLOUR_PURPLE = 'purple'

    COLOURS = [
        (COLOUR_RED, COLOUR_RED),
        (COLOUR_BLUE, COLOUR_BLUE),
        (COLOUR_GREEN, COLOUR_GREEN),
        (COLOUR_ORANGE, COLOUR_ORANGE),
        (COLOUR_PURPLE, COLOUR_PURPLE),
    ]

    EFFICIENCY_A = 'A'
    EFFICIENCY_B = 'B'
    EFFICIENCY_C = 'C'
    EFFICIENCY_D = 'D'
    EFFICIENCY_E = 'E'

    FUEL_EFFICIENCY = [
        (EFFICIENCY_A, EFFICIENCY_A),
        (EFFICIENCY_B, EFFICIENCY_B),
        (EFFICIENCY_C, EFFICIENCY_C),
        (EFFICIENCY_D, EFFICIENCY_D),
        (EFFICIENCY_E, EFFICIENCY_E),
    ]

    make = models.CharField(max_length=50, choices=MAKES)
    manufacture_date = models.DateField()
    colour = models.CharField(max_length=25, choices=COLOURS)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    fuel_efficiency_rating = models.CharField(max_length=1, choices=FUEL_EFFICIENCY)
    has_ejector_seat = models.BooleanField(default=False)

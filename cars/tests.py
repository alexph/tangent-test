from django.test import TestCase, RequestFactory
from .models import Car
from .factories import CarFactory
import json


class AddCarTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_add_car_valid(self):
        data = {
            'make': Car.MAKE_ASTON_MARTIN,
            'manufacture_date': '2010-01-01',
            'colour': Car.COLOUR_BLUE,
            'sale_price': 99.99,
            'fuel_efficiency_rating': Car.EFFICIENCY_A,
            'has_ejector_seat': False
        }

        response = self.client.post('/add-car/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_add_car_invalid(self):
        response = self.client.post('/add-car/', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)

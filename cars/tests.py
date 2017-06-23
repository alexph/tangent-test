from django.test import TestCase, RequestFactory
from .models import Car
from .factories import CarFactory
import factory
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


class EjectorCountTestCase(TestCase):
    def setUp(self):
        self.cars = factory.create_batch(CarFactory, 5, has_ejector_seat=True)

    def tearDown(self):
        for car in self.cars:
            car.delete()

    def test_ejector_count(self):
        response = self.client.get('/ejector-count/')

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertIn('count', data)
        self.assertEqual(len(self.cars), data['count'])


class MostCommonFuelRatingTestCase(TestCase):
    def setUp(self):
        self.cars = factory.create_batch(CarFactory, 5, has_ejector_seat=True)
        self.control = CarFactory(fuel_efficiency_rating=Car.EFFICIENCY_C)

    def tearDown(self):
        for car in self.cars:
            car.delete()
        self.control.delete()

    def test_ejector_count(self):
        response = self.client.get('/most-common-fuel-rating/')

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertIn('fuel_efficiency_rating', data)
        self.assertEqual(self.control.fuel_efficiency_rating, data['fuel_efficiency_rating'])

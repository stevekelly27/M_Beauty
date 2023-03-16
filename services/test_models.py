"""Imports from django and the service model."""
from django.test import TestCase
from .models import Service


class TestServiceModels(TestCase):

    """
    Test on the string method in the service model.
    """

    def test_string_method_returns_name(self):
        """Function to check the string method returns the service name."""
        service = Service.objects.create(
            name='Test string',
            service_type='GEL',
            price='50')
        self.assertEqual(str(service), 'Test string')

"""Imports from django and the service form."""
from django.test import TestCase
from .forms import ServiceForm


class TestServiceForm(TestCase):

    """
    Tests to check the service form
    Checks on if the add services
    form displays all specified fields,
    and if the correct error messages
    are displayed.
    """

    def test_fields_are_explicit_in_metaclass(self):
        """Function to check whether specified form fields display."""
        form = ServiceForm()
        self.assertEqual(form.Meta.fields, ['name', 'service_type', 'description', 'price', 'image'])

    def test_service_name_is_required(self):
        """Function to check whether missed service name generates an error."""
        form = ServiceForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_service_type_is_required(self):
        """Function to check missed service type generates an error."""
        form = ServiceForm({'service_type': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('service_type', form.errors.keys())
        self.assertEqual(
            form.errors['service_type'][0],
            'This field is required.'
            )

    def test_service_price_is_required(self):
        """Function to check missed service price generates an error."""
        form = ServiceForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

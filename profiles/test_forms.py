from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

    def test_form_fields(self):
        """
        Test that the form has the expected fields
        """
        form = UserProfileForm()
        expected_fields = [
            'default_phone_number',
            'default_postcode',
            'default_town_or_city',
            'default_street_address1',
            'default_street_address2',
            'default_county',
            'default_country',
        ]
        self.assertCountEqual(form.fields.keys(), expected_fields)

    def test_form_valid(self):
        """
        Test that the form is valid when all required fields are provided
        """
        data = {
            'default_phone_number': '+123456789',
            'default_postcode': '12345',
            'default_town_or_city': 'Test City',
            'default_street_address1': 'Test Address 1',
            'default_street_address2': 'Test Address 2',
            'default_county': 'Test County',
        }
        form = UserProfileForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_placeholder_and_class_attributes(self):
        """
        Test that the form fields have the expected placeholder and class attributes
        """
        form = UserProfileForm()
        expected_placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }
        for field_name, placeholder in expected_placeholders.items():
            field = form.fields.get(field_name)
            self.assertIsNotNone(field)
            self.assertEqual(
                field.widget.attrs.get('placeholder'), placeholder)
            self.assertEqual(
                field.widget.attrs.get(
                    'class'), 'border-black rounded-0 profile-form-input')

    def test_form_autofocus_attribute(self):
        """
        Test that the first form field has the autofocus attribute
        """
        form = UserProfileForm()
        expected_field_name = 'default_phone_number'
        expected_autofocus_value = True
        first_field = list(form.fields.values())[0]
        self.assertEqual(
            first_field.widget.attrs.get(
                'autofocus'), expected_autofocus_value)

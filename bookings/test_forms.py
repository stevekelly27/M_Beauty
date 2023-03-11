from django.test import TestCase
from datetime import date
from .models import Booking
from django.db import IntegrityError, transaction
from .forms import BookingForm, BookingFormAdmin


class BookingFormTest(TestCase):
    def test_valid_booking_form(self):
        """
        Test that a valid form is saved to the database.
        """
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'date': date.today(),
            'time': '10AM',
            'service': 'Gel'
        }
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())
        booking = form.save()
        self.assertEqual(booking.first_name, 'Jane')
        self.assertEqual(booking.last_name, 'Doe')
        self.assertEqual(booking.date, date.today())
        self.assertEqual(booking.time, '10AM')
        # test meta_class of unique_together in likeability model
        try: 
            with transaction.atomic():
                form_data = {
                    'first_name': 'second Jane',
                    'last_name': 'second Doe',
                    'date': date.today(),
                    'time': '10AM',
                    'service': 'Gel'
                }
                form = BookingForm(data=form_data)
                booking = form.save()

            self.fail('Duplicate question allowed.')
        except IntegrityError: 
            pass   # Duplicate question not allowed. Unique_together in Meta Class work

    def test_invalid_booking_form(self):
        """
        Test that an invalid form is not saved to the database.
        """
        form_data = {
            'first_name': '',
            'last_name': '',
            'date': '',
            'time': '',
            'service': ''
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)

        
class BookingFormAdminTest(TestCase):
    def test_valid_booking_form_admin(self):
        """
        Test that a valid form is saved to the database.
        """
        form_data = {
            'user': '',
            'first_name': 'Jane',
            'last_name': 'Doe',
            'date': date.today(),
            'time': '10AM',
            'service': 'Gel'
        }
        form = BookingFormAdmin(data=form_data)
        self.assertTrue(form.is_valid())
        booking = form.save()
        self.assertEqual(booking.first_name, 'Jane')
        self.assertEqual(booking.last_name, 'Doe')
        self.assertEqual(booking.date, date.today())
        self.assertEqual(booking.time, '10AM')
        self.assertEqual(booking.service, 'Gel')

    def test_invalid_booking_form_admin(self):
        """
        Test that an invalid form is not saved to the database.
        """
        form_data = {
            'user': '',
            'first_name': '',
            'last_name': '',
            'date': '',
            'time': '',
            'service': ''
        }
        form = BookingFormAdmin(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)

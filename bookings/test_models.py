from datetime import date
from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Booking
from services.models import Service


class BookingModelTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            date=date.today(),
            time="10AM",
            first_name='John',
            last_name='Doe',
            service=GEL,
            user='john Doe',
        )

    def test_booking_str(self):
        self.assertEqual(str(self.booking), f'{date.today()} 10AM')

    def test_past_date(self):
        self.assertTrue(self.booking.past_date)
    
    def test_validate_date_past(self):
        with self.assertRaises(ValidationError):
            Booking(date=date(2023, 3, 9), time='10AM', first_name='Jane', last_name='Doe', service=GEL, user='John Doe').full_clean()
    
    def test_validate_date_future(self):
        future_date = date.today().replace(year=date.today().year + 1)
        booking = Booking(date=future_date, time='10AM', first_name='Jane', last_name='Doe', service=GEL, user='John Doe')
        booking.full_clean() # should not raise a ValidationError

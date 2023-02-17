from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    """
    Booking model for booking database.
    """

    TIME_LIST = (
        (0, '10AM'),
        (1, '11AM'),
        (2, '12PM'),
        (3, '1PM'),
        (4, '2PM'),
        (5, '3PM'),
        (6, '4PM'),
        (7, '5PM'),
        (8, '6PM'),
        (9, '7PM'),
    )

    def validate_date(self):
        """
        Method to display error message if date selected is in the past.
        """
        if self < date.today():
            raise ValidationError("Date cannot be in the past")

    date = models.DateField(
        validators=[validate_date]
        )

    time = models.IntegerField(choices=TIME_LIST)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    service = models.ForeignKey(
        'services.Service',
        on_delete=models.CASCADE,
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="timeslot")

    def __str__(self):
        """
        Method to display booking instance by date, time and stylist.
        """ 
        return f'{self.date} {self.get_time_display()}'

    class Meta:
        """
        Class to ensure booking is classified as
        unique by date and time.
        """
        unique_together = ('date', 'time')

    @property
    def past_date(self):
        """
        Decorator to check if date is in the past.
        """
        today = date.today()
        if self.date < today:
            return True

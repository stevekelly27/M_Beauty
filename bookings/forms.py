from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    """
    Class for date input widget.
    """
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """
    Booking form used to book appointments.
    Inspired from codemy.
    """

    class Meta:
        """
        Class to define booking form fields, labels and widgets.
        """
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'date',
            'time',
            'service']
        labels = {
            'first_name': 'Client First Name',
            'last_name': 'Client Last Name'
        }
        widgets = {
            'date': DateInput(),
        }

    def clean_first_name(self):
        """
        Method to capitalize first names from bookings form.
        """
        return self.cleaned_data['first_name'].capitalize()

    def clean_last_name(self):
        """
        Method to capitalize last names from bookings form.
        """
        return self.cleaned_data['last_name'].capitalize()

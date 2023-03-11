from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    """
    Class for date input widget.
    """
    input_type = 'date'


class BookingFormAdmin(forms.ModelForm):
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
            'user',
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

    def clean(self):

        cleaned_data = super().clean()
        dt = cleaned_data.get('date')
        time = cleaned_data.get('time')

        try:
            Booking.objects.get(date=cleaned_data['date'], time=cleaned_data['time'])
        except Booking.DoesNotExist:
            pass
        else:
            raise forms.ValidationError('Booking for this date and time already exists')

        return cleaned_data  # or self.cleaned_data


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

    def clean(self):

        cleaned_data = super().clean()
        dt = cleaned_data.get('date')
        time = cleaned_data.get('time')

        try:
            Booking.objects.get(date=cleaned_data['date'], time=cleaned_data['time'])
        except Booking.DoesNotExist:
            pass
        else:
            raise forms.ValidationError('Booking for this date and time already exists')

        return cleaned_data  # or self.cleaned_data

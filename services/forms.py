"""Imports from django and service model."""
from django import forms
from .models import Service
from products.widgets import CustomClearableFileInput


class ServiceForm(forms.ModelForm):
    """
    Service form used to add services.
    """

    class Meta:
        """
        Class to define service form fields and labels.
        """
        model = Service
        fields = ['name', 'service_type', 'description', 'price', 'image']
        labels = {
            'name': 'Service name',
            'price': 'Price (€)'
        }

        image = forms.ImageField(
            label='Image', required=False, widget=CustomClearableFileInput)

    def clean_name(self):
        """
        Method to capitalize service name from service form.
        """
        return self.cleaned_data['name'].capitalize()

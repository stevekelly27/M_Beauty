from django.test import TestCase
from .forms import OrderForm
from .models import Order


class TestOrderForm(TestCase):
    
    def test_order_form_valid_data(self):
        form = OrderForm({
            'full_name': 'John Smith',
            'email': 'john@example.com',
            'phone_number': '1234567890',
            'street_address1': '123 Main St',
            'town_or_city': 'Anytown',
            'postcode': '12345',
            'country': 'US',
        })
        self.assertTrue(form.is_valid())
        
    def test_order_form_missing_required_data(self):
        form = OrderForm({
            'full_name': 'John Smith',
            'email': 'john@example.com',
            'phone_number': '',
            'street_address1': '',
            'town_or_city': '',
            'postcode': '',
            'country': '',
        })
        form_data = {
            'first_name': 'second John',
            'last_name': 'second Doe',
            'date': date.today(),
            'time': '09:00:00',
            'service': 'Haircut'
        }
        form = BookingForm(data=form_data)
        booking = form.save()
        self.assertEqual(form.errors['phone_number'], ['This field is required.'])
        self.assertEqual(form.errors['street_address1'], ['This field is required.'])
        self.assertEqual(form.errors['town_or_city'], ['This field is required.'])
        self.assertEqual(form.errors['country'], ['This field is required.'])
        
    def test_order_form_fields_labels(self):
        form = OrderForm()
        self.assertFalse(form.fields['full_name'].label)
        self.assertFalse(form.fields['email'].label)
        self.assertFalse(form.fields['phone_number'].label)
        self.assertFalse(form.fields['street_address1'].label)
        self.assertFalse(form.fields['street_address2'].label)
        self.assertFalse(form.fields['town_or_city'].label)
        self.assertFalse(form.fields['postcode'].label)
        self.assertFalse(form.fields['county'].label)
        
    def test_order_form_fields_placeholder(self):
        form = OrderForm()
        self.assertEqual(form.fields['full_name'].widget.attrs['placeholder'], 'Full Name *')
        self.assertEqual(form.fields['email'].widget.attrs['placeholder'], 'Email Address *')
        self.assertEqual(form.fields['phone_number'].widget.attrs['placeholder'], 'Phone Number *')
        self.assertEqual(form.fields['street_address1'].widget.attrs['placeholder'], 'Street Address 1 *')
        self.assertEqual(form.fields['street_address2'].widget.attrs['placeholder'], 'Street Address 2')
        self.assertEqual(form.fields['town_or_city'].widget.attrs['placeholder'], 'Town or City *')
        self.assertEqual(form.fields['postcode'].widget.attrs['placeholder'], 'Postal Code')
        self.assertEqual(form.fields['county'].widget.attrs['placeholder'], 'County, State or Locality')
        
    def test_order_form_fields_classes(self):
        form = OrderForm()
        self.assertEqual(form.fields['full_name'].widget.attrs['class'], 'stripe-style-input')
        self.assertEqual(form.fields['email'].widget.attrs['class'], 'stripe-style-input')
        self.assertEqual(form.fields['phone_number'].widget.attrs['class'], 'stripe-style-input')
        self.assertEqual(form.fields['street_address1'].widget.attrs['class'], 'stripe-style-input')
        self.assertEqual(form.fields['street_address2'].widget.attrs['class'], 'stripe-style-input')
        self.assertEqual(form.fields['town_or_city'].widget.attrs['class'], 'stripe-style-input')
        self.assertEqual(form.fields['postcode'].widget.attrs['class'], 'stripe-style-input')
        self.assertEqual(form.fields['county'].widget.attrs['class'], 'stripe-style-input')

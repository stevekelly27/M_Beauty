# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth.models import User
# from django.conf import settings

# from .models import Order
# from .views import checkout, cache_checkout_data
# from .forms import OrderForm

# import json


# class CheckoutViewTest(TestCase):
#     def setUp(self):
#         self.url = reverse('checkout')
#         self.test_user = User.objects.create_user(
#             username='testuser',
#             password='12345'
#         )

#     def test_checkout_view_GET(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'checkout/checkout.html')
#         self.assertIsInstance(response.context['order_form'], OrderForm)

#     def test_checkout_view_POST_valid_form(self):
#         bag = {
#             '1': 1,
#             '2': 2
#         }
#         self.client.login(username='testuser', password='12345')
#         response = self.client.post(self.url, {
#             'full_name': 'Test User',
#             'email': 'testuser@example.com',
#             'phone_number': '1234567890',
#             'country': 'US',
#             'postcode': '12345',
#             'town_or_city': 'Test City',
#             'street_address1': '123 Test St',
#             'street_address2': '',
#             'county': 'Test County',
#             'client_secret': 'pi_abc123_secret',
#             'save_info': False
#         }, follow=True)

#         self.assertRedirects(response, reverse('checkout_success', args=[1]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'checkout/checkout_success.html')
#         self.assertEqual(Order.objects.count(), 1)
#         order = Order.objects.first()
#         self.assertEqual(order.full_name, 'Test User')
#         self.assertEqual(order.email, 'testuser@example.com')
#         self.assertEqual(order.phone_number, '1234567890')
#         self.assertEqual(order.country, 'US')
#         self.assertEqual(order.postcode, '12345')
#         self.assertEqual(order.town_or_city, 'Test City')
#         self.assertEqual(order.street_address1, '123 Test St')
#         self.assertEqual(order.street_address2, '')
#         self.assertEqual(order.county, 'Test County')
#         self.assertEqual(order.original_bag, json.dumps(bag))
#         self.assertEqual(order.stripe_pid, 'pi_abc123_secret')
#         self.assertFalse(order.bookings.all())

#     def test_checkout_view_POST_invalid_form(self):
#         self.client.login(username='testuser', password='12345')
#         response = self.client.post(self.url, {})
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'checkout/checkout.html')
#         self.assertIsInstance(response.context['order_form'], OrderForm)

#     def test_checkout_view_POST_empty_bag(self):
#         self.client.login(username='testuser', password='12345')
#         response = self.client.post(self.url, {
#             'full_name': 'Test User',
#             'email': 'testuser@example.com',
#             'phone_number': '1234567890',
#             'country': 'US',
#             'postcode': '12345',
#             'town_or_city': 'Test City',
#             'street_address1': '123 Test St',
#             'street_address2': '',
#             'county': 'Test County',
#             'client_secret': 'pi_abc123_secret',
#             'save_info': False
#         }, follow=True)

#         self.assertRedirects(response, reverse('view_bag'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'bag/bag.html')
#         self.assertContains(response, 'Your bag is currently empty')

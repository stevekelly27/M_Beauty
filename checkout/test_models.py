# from django.test import TestCase
# from django_countries import countries
# from django.contrib.auth.models import User

# from profiles.models import UserProfile
# from products.models import Product
# from .models import Order, OrderLineItem


# class TestOrderModels(TestCase):

#     def setUp(self):
#         # Create a new user object for testing
#         self.user = User.objects.create_user(
#             username='testuser', email='testuser@example.com', password='testpassword')

#         # Check if a UserProfile object exists for the user object
#         try:
#             self.user_profile = self.user.userprofile
#         except UserProfile.DoesNotExist:
#             # If UserProfile object doesn't exist, create a new one
#             self.user_profile = UserProfile.objects.create(user=self.user)

#         # Create a new Order object for testing
#         self.order = Order.objects.create(
#             user_profile=self.user_profile,
#             full_name='Test User',
#             phone_number='1234567890',
#             country='US',
#             postcode='12345',
#             town_or_city='Test City',
#             street_address1='123 Test Street',
#             street_address2='Test Address 2',
#             county='Test County',
#             date='2021-01-01',
#         )

#         # Create a new OrderLineItem object for testing
#         self.order_line_item = OrderLineItem.objects.create(
#             order=self.order,
#             product_id=1,
#             quantity=1,
#         )

#     def test_order_number_generated_on_save(self):
#         self.assertTrue(self.order.order_number)

#     def test_order_update_total(self):
#         self.assertEqual(self.order.total, self.order_line_item.lineitem_total)


#     def test_orderlineitem_save(self):
#         order = Order.objects.create(
#             user_profile=self.user_profile,
#             full_name='John Smith',
#             email='johnsmith@example.com',
#             phone_number='555-555-5555',
#             country=countries.US,
#             town_or_city='New York',
#             street_address1='123 Main St',
#             order_total=9.99,
#         )
#         line_item = OrderLineItem.objects.create(
#             order=order,
#             product=self.product,
#             quantity=2,
#         )
#         self.assertEqual(line_item.lineitem_total, 19.98)

#     def test_orderlineitem_str(self):
#         order = Order.objects.create(
#             user_profile=self.user_profile,
#             full_name='John Smith',
#             email='johnsmith@example.com',
#             phone_number='555-555-5555',
#             country=countries.US,
#             town_or_city='New York',
#             street_address1='123 Main St',
#             order_total=9.99,
#         )
#         line_item = OrderLineItem.objects.create(
#             order=order,
#             product=self.product,
#             quantity=2,
#         )
#         self.assertEqual(str(line_item), f'SKU {self.product.sku} on order {order.order_number}')

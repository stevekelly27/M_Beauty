# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import UserProfile


# class TestModels(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='testuser',
#             email='test@example.com',
#             password='testpass'
#         )
#         self.userprofile = UserProfile.objects.create(
#             user=self.user,
#             default_phone_number='51234567890',
#             default_street_address1='123 forn St.',
#             default_town_or_city='Anytown',
#             default_county='Any',
#             default_postcode='12345',
#             default_country='UK'
#         )

#     def test_userprofile_creation(self):
#         self.assertEqual(UserProfile.objects.count(), 1)
#         self.assertEqual(str(self.userprofile), 'testuser')

#     def test_create_or_update_user_profile(self):
#         self.assertEqual(UserProfile.objects.count(), 1)
#         User.objects.create_user(
#             username='testuser2',
#             email='test2@example.com',
#             password='testpass'
#         )
#         self.assertEqual(UserProfile.objects.count(), 2)
#         User.objects.filter(username='testuser2').update(email='newemail@example.com')
#         self.assertEqual(UserProfile.objects.filter(user__email='newemail@example.com').count(), 1)
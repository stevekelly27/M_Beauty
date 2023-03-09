# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from django.contrib.messages import get_messages
# from django.core.management import call_command
# from mixer.backend.django import mixer

# from .models import UserProfile
# from checkout.models import Order
# from .forms import UserProfileForm


# class ProfileViewTestCase(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         # Delete all existing UserProfiles
#         UserProfile.objects.all().delete()

#     @classmethod
#     def setUpTestData(cls):
#         # Create a test user and profile
#         cls.client = Client()
#         cls.user = get_user_model().objects.create_user(
#             username='testuser',
#             email='testuser@test.com',
#             password='testpassword'
#         )
#         cls.profile = mixer.blend(UserProfile, user=cls.user)

#     def setUp(self):
#         # Log in the test user and reset the database
#         self.client.force_login(self.user)
#         call_command('flush', verbosity=0, interactive=False)

#     def test_profile_view(self):
#         # Test that the profile view displays the profile form
#         url = reverse('profile')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'profiles/profile.html')
#         self.assertContains(response, 'Edit Profile')
#         self.assertIsInstance(response.context['form'], UserProfileForm)
#         self.assertTrue(response.context['on_profile_page'])

#     def test_profile_view_post_valid_form(self):
#         # Test that the profile view updates the profile with valid form data
#         url = reverse('profile')
#         data = {
#             'default_phone_number': '1234567890',
#             'default_street_address1': '123 Main St',
#             'default_town_or_city': 'City',
#             'default_postcode': '12345',
#             'default_country': 'US'
#         }
#         response = self.client.post(url, data)
#         self.assertRedirects(response, url)
#         self.assertEqual(get_messages(response.wsgi_request)[0].message, 'Profile updated successfully')
#         self.profile.refresh_from_db()
#         self.assertEqual(self.profile.default_phone_number, data['default_phone_number'])
#         self.assertEqual(self.profile.default_street_address1, data['default_street_address1'])
#         self.assertEqual(self.profile.default_town_or_city, data['default_town_or_city'])
#         self.assertEqual(self.profile.default_postcode, data['default_postcode'])
#         self.assertEqual(self.profile.default_country, data['default_country'])

#     def test_profile_view_post_invalid_form(self):
#         # Test that the profile view handles invalid form data gracefully
#         url = reverse('profile')
#         data = {
#             'default_phone_number': '123',
#             'default_street_address1': '',
#             'default_town_or_city': '',
#             'default_postcode': '',
#             'default_country': ''
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, 200)
#         self.assertFalse(response.context['form'].is_valid())
#         self.assertContains(response, 'Update failed. Please ensure the form is valid.')
#         self.assertFalse(UserProfile.objects.filter(user=self.user).exists())

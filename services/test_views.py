"""Imports from django and the service model."""
from django.test import TestCase
from .models import Service


class TestServiceViews(TestCase):

    """
    Tests to check service views
    Checks on if the services
    add/edit/delete pages open and
    if a user can add/edit/delete
    services
    """

    # Test if the services page opens
    def test_get_services(self):
        """Function to check whether the services page displays."""
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/services.html')

    # Test if the add services page opens
    
    def test_can_add_services_page(self):
        """Function to check whether the add services page displays."""
        response = self.client.get('/services/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/add_services.html')

    # Test if a service can be added
    def test_can_add_service(self):
        """Function to check whether a service can be added."""
        response = self.client.post(
            '/services/add/',
            {
                'name': 'Test add service',
                'service_type': 'GEL',
                'price': '50'
            }
        )
        self.assertRedirects(response, '/services/')

    # Test if the edit services page opens
    def test_get_edit_services_page(self):
        """Function to check whether the edit service page displays."""
        service = Service.objects.create(
            name='Test edit page',
            description='All designs included',
            service_type='GEL',
            price='50',
            image='img.JPG'
        )
        response = self.client.get(f'/services/edit/{service.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/edit_services.html')

    # Test if a service can be edited
    def test_can_edit_service(self):
        """Function to check whether a service can be edited."""
        service = Service.objects.create(
            name='Test edit service',
            description='All designs included',
            service_type='GEL',
            price='50',
            image='img.JPG'
        )
        response = self.client.post(
            f'/services/edit/{service.id}',
            {
                'name': 'Test edit check',
                'description': 'All designs included',
                'service_type': 'GEL',
                'price': '40',
                'image': 'img.JPG'
            }
        )
        self.assertRedirects(response, '/services/')
        updated_item = Service.objects.get(id=service.id)
        self.assertEqual(updated_item.name, 'Test edit check')

    # Test if the delete services page opens
    def test_get_delete_services_page(self):
        """Function to check whether the delete services page displays."""
        service = Service.objects.create(
            name='Test delete page',
            description='All designs included',
            service_type='GEL',
            price='50',
            image='img.JPG'
        )
        response = self.client.get(f'/services/delete/{service.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'services/delete_services.html'
            )

    # Test if a service can be deleted
    def test_can_delete_item(self):
        """Function to check whether a service can be deleted."""
        service = Service.objects.create(
            name='Test delete',
            description='All designs included',
            service_type='GEL',
            price='50',
            image='img.JPG'
        )
        existing_items = Service.objects.filter(id=service.id)
        self.assertEqual(len(existing_items), 1)
        response = self.client.post(f'/services/delete/{service.id}')
        self.assertRedirects(response, '/services/')
        existing_items = Service.objects.filter(id=service.id)
        self.assertEqual(len(existing_items), 0)
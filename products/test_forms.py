from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .forms import ProductForm
from .models import Product, Category


class ProductFormTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.valid_data = {
            'name': 'Test Product',
            'description': 'This is a test product.',
            'price': 9.99,
            'category': self.category.id,
            'image': SimpleUploadedFile('test_image.jpg', b'content')
        }

    def test_blank_data(self):
        form = ProductForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            len(form.errors), 4)  # name, price, and category are required

    def test_invalid_price(self):
        invalid_data = self.valid_data.copy()
        invalid_data['price'] = 'not a price'
        form = ProductForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors)

    def test_invalid_category(self):
        invalid_data = self.valid_data.copy()
        invalid_data['category'] = 1000  # category ID that doesn't exist
        form = ProductForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors)

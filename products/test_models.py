from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User


class TestProductsModel(TestCase):

    def test_create_product(self):
        product = Product(name='Test Product',
                          description='Some test content.',
                          stock_level='10',
                          in_stock='True')
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.description, "Some test content.")
        self.assertFalse(product.image)
        self.assertFalse(product.price)
        self.assertEqual(product.stock_level, '10')
        self.assertEqual(product.in_stock, "True")

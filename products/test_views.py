# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth.models import User
# from .models import Product, Category
# from .forms import ProductForm


# class TestViews(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.products_url = reverse('products')
#         self.add_product_url = reverse('add_product')
#         self.edit_product_url = reverse('edit_product', args=[1])
#         self.delete_product_url = reverse('delete_product', args=[1])
#         self.user = User.objects.create_user(
#             username='testuser',
#             password='testpass'
#         )
#         self.category = Category.objects.create(name='TestCategory')
#         self.product = Product.objects.create(
#             name='TestProduct',
#             price=10.00,
#             category=self.category
#         )
#         self.product_form_data = {
#             'name': 'TestProduct2',
#             'description': 'This is a test product',
#             'price': 20.00,
#             'category': self.category.id,
#             'image': ''
#         }
#         self.edit_product_form_data = {
#             'name': 'TestProduct2',
#             'description': 'This is an edited test product',
#             'price': 30.00,
#             'category': self.category.id,
#             'image': ''
#         }

#     def test_all_products_view(self):
#         response = self.client.get(self.products_url)
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'products/products.html')

#     def test_product_detail_view(self):
#         response = self.client.get(reverse('product_detail', args=[self.product.id]))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'products/product_detail.html')

#     def test_add_product_view(self):
#         self.client.login(username='testuser', password='testpass')
#         response = self.client.post(self.add_product_url, self.product_form_data)
#         self.assertEquals(response.status_code, 302)
#         self.assertTrue(Product.objects.filter(name='TestProduct2').exists())

#     def test_edit_product_view(self):
#         self.client.login(username='testuser', password='testpass')
#         response = self.client.post(self.edit_product_url, self.edit_product_form_data)
#         self.assertEquals(response.status_code, 302)
#         self.assertTrue(Product.objects.filter(description='This is an edited test product').exists())

    # def test_delete_product_view(self):
    #     self.client.login(username='testuser', password='testpass')
    #     response = self.client.post(self.delete_product_url)
    #     self.assertEquals(response.status_code, 302)
    #     self.assertFalse(Product.objects.filter(name='TestProduct').exists())
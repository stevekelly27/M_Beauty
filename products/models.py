from django.db import models
from django.core.exceptions import ValidationError
import datetime
from bookings.models import Booking


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product (models.Model):
    product_id = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_level = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    booking = {
        
    }

    def save(self, *args, **kwargs):
        if self.stock_level <= 0:
            self.in_stock = False
        else:
            self.in_stock = True
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

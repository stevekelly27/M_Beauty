from decimal import Decimal
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class Service(models.Model):
    """
    Service model for service database.
    """

    class ServiceType(models.TextChoices):
        """
        Service type field options.
        """

        GEL = 'GEL', 'Gel'
        SHELLAC = 'SHELLAC', 'Shellac'
        MANICURE = 'MANICURE', 'Manicure'
        BROWS = 'BROWS', 'Brows'
        HENNA = 'HENNA', 'Henna'
        SHAPE_TINT = 'SHAPE_TINT', 'Shape_tint'

    name = models.CharField(max_length=100, unique=True)
    service_type = models.CharField(
        max_length=20,
        choices=ServiceType.choices,
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('12.00')),
                    MaxValueValidator(Decimal('250.00'))]
        )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """
        Method to display service instance by its name.
        """
        return str(self.name)
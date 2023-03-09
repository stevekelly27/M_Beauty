from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    in_stock = True
    booking_total = 0
    product = get_object_or_404(Product, name='Booking deposit')
    booking_id = product.id

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            if item_id == booking_id:
                booking_total += item_data * product.price
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

    if (total - booking_total) > 0:
        if (total - booking_total) < settings.FREE_DELIVERY_THRESHOLD:
            delivery = (total - booking_total) * Decimal(
                settings.STANDARD_DELIVERY_PERCENTAGE / 100)
            free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
        else:
            delivery = 0
            free_delivery_delta = 0
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'in_stock': in_stock,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

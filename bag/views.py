from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
    )
from django.contrib import messages
from bookings.models import Booking
from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    bag = request.session.get('bag', {})

    if product.name == 'Booking deposit':
        redirect_url = 'bookings'
    else:
        redirect_url = request.POST.get('redirect_url')

    if product.name == 'Booking deposit':
        quantity = 1
    else:
        quantity = int(request.POST.get('quantity'))

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)

        request.session['bag'] = bag
        if 'quantity' in request.POST:
            quantity = int(request.POST['quantity'])
        product = get_object_or_404(Product, name='Booking deposit')
        booking_id = product.id
        if int(item_id) == int(booking_id):
            latest_booking = Booking.objects.filter(user=request.user).order_by('-id')[:quantity]
            for lb in latest_booking:
                lb.delete()

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

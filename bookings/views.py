from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from products.models import Product
from django.utils import timezone


def bookings(request):
    """
    Function to view bookings page.
    """

    if request.user.is_superuser:
        booking = Booking.objects.all().order_by('date')
        context = {
            'bookings': booking
        }
    else:
        user_filter = Booking.objects.filter(user__in=[request.user])
        booking = user_filter.order_by('date')
        context = {
            'bookings': booking
        }
    return render(request, 'bookings/bookings.html', context)


def add_bookings(request):
    """
    Function to view add bookings page.
    The get request returns the add bookings form.
    Different forms for admin and non-admin users.
    The post request checks the form is valid, saves
    if valid and returns bookings page with the success
    message. If form is invalid, error message is
    displayed.
    """
    if request.method == 'POST':

        form = BookingForm(request.POST)
        product = get_object_or_404(Product, name='booking')
        context = {
            'form': form
        }
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(
                request,
                'Request successful',
                extra_tags='successful_request'
            )
            return redirect('add_to_bag', item_id=product.id)
        else:
            messages.error(
                request,
                'Request unsuccessful - address errors',
                extra_tags='unsuccessful_request'
                )
            return render(request, 'bookings/add_bookings.html', context)

    else:
        form = BookingForm
        context = {
            'form': form
        }
    return render(request, 'bookings/add_bookings.html', context)


def delete_bookings(request, booking_id):
    """
    Function to view delete bookings page.
    The get request returns the delete bookings page.
    The post request deletes the booking,
    returns booking page and
    displays the success message on the bookings page.
    """

    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        created = booking.created
        paid = booking.paid
        booking.delete()
        messages.success(
            request,
            'Request successful',
            extra_tags='successful_request'
        )

        time_threshould = timezone.now() - timedelta(minuets=30)

        if (created == timezone.now() or created >= time_threshould) and paid == False:
            bag = request.session.get('bag', {})
            product = get_object_or_404(Product, name='booking')
            item_id = product._check_id_field()
        
        if item_id in list(bag.keys()):
            quantity = bag[item_id]
            if quantity > 1:
                bag[item_id] -= quantity
            else:
                bag.pop(item_id)
            
            request.session['bag'] = bag

        return redirect('bookings')
    context = {
        'bookings': booking
    }
    return render(request, 'bookings/delete_bookings.html', context)

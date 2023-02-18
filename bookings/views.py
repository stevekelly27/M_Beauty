from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


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
            return redirect('bookings')
        else:
            messages.error(
                request,
                'Request unsuccessful - address errors',
                extra_tags='unsuccessful_request'
                )
            return render(request, 'bookings/bookings.html', context)


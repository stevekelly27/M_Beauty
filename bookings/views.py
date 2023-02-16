from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingFormAdmin, BookingForm


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

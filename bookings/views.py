from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from .forms import BookingForm, BookingFormAdmin
from products.models import Product
from django.utils import timezone
from datetime import datetime, timedelta


@login_required(login_url='/accounts/login/')
def bookings(request):
    """
    Function to view bookings page.
    """

    if request.user.is_superuser:
        # product = Product.objects.all.filter('bookings')
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


@login_required(login_url='/accounts/login/')
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
        if request.user.is_superuser:
            form = BookingFormAdmin(request.POST)
            context = {
                'form': form
            }
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    'Request successful',
                    extra_tags='successful_request'
                )
                return redirect('bookings')
            else:
                messages.error(
                    request,
                    'Request unsuccessful - Please make sure all the fields have been filled out properly on the form',
                    extra_tags='unsuccessful_request'
                    )
                return render(request, 'bookings/add_bookings.html', context)

        else:
            form = BookingForm(request.POST)
            product = get_object_or_404(Product, name='Booking deposit')
            context = {
                'form': form
            }
            print("form", form)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                #booking.paid = False
                booking.save()
                return redirect('add_to_bag', item_id=product.id)
            else:
                messages.error(
                    request,
                    'Request unsuccessful - sorry, this slot has been filled. Please choose another time.',
                    extra_tags='unsuccessful_request'
                    )
                return render(request, 'bookings/add_bookings.html', context)

    else:
        if request.user.is_superuser:
            form = BookingFormAdmin
        else:
            form = BookingForm
        context = {
            'form': form
        }

    return render(request, 'bookings/add_bookings.html', context)

@login_required(login_url='/accounts/login/')
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

        time_threshould = timezone.now() - timedelta(minutes=30)
        #https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python
        difference = created - time_threshould

        seconds_in_day = 24 * 60 * 60
        minutesdiff = divmod(difference.days * seconds_in_day + difference.seconds, 60)[0]
        print("check", minutesdiff, paid)

        if (created.date() == timezone.now().date() or minutesdiff >= 0) and paid == False:
            print("here")

            bag = request.session.get('bag', {})
            product = get_object_or_404(Product, name='Booking deposit')
            item_id = str(product.id)

            if item_id in list(bag.keys()):
                quantity = int(bag[item_id])
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

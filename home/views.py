from django.shortcuts import render
# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def price_list(request):
    """ A view to return the price-list page """
    return render(request, 'home/price_list.html')


def contact(request):
    """ A view to return the contact page """
    return render(request, 'home/contact.html')

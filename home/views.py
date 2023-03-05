from django.shortcuts import render
# Create your views here.


def index(request):
    """ A view to return the index page """
    #del request.session['bag']
    return render(request, 'home/index.html')


def price_list(request):
    """ A view to return the index page """
    #del request.session['bag']
    return render(request, 'home/price-list.html')

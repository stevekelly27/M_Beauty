from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Service
from .forms import ServiceForm


def services(request):
    """
    Function to view services page.
    Services filtered by service type.
    """

    cut_services = Service.objects.filter(
        service_type__contains='GEL').order_by('name')
    colour_services = Service.objects.filter(
        service_type__contains='SHELLAC').order_by('name')
    style_services = Service.objects.filter(
        service_type__contains='BROW').order_by('name')
    style_services = Service.objects.filter(
        service_type__contains='WAX').order_by('name')
    return render(request, 'services/services.html', {
        'gel_nails': cut_services,
        'shellac': shellac,
        'eyebrows': eyebrows,
        'waxing': waxing,})

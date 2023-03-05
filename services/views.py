from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Service
from .forms import ServiceForm


def services(request):
    """
    Function to view services page.
    Services filtered by service type.
    """

    gel_nail_services = Service.objects.filter(
        service_type__contains='GEL').order_by('name')
    shellac_services = Service.objects.filter(
        service_type__contains='SHELLAC').order_by('name')
    manicure_services = Service.objects.filter(
        service_type__contains='MANICURE').order_by('name')
    brow_services = Service.objects.filter(
        service_type__contains='BROWS').order_by('name')
    henna_brow_services = Service.objects.filter(
        service_type__contains='HENNA').order_by('name')
    shape_tint_services = Service.objects.filter(
        service_type__contains='SHAPE_TINT').order_by('name')
    return render(request, 'services/services.html', {
        'gel_nail_services': gel_nail_services,
        'shellac_services': shellac_services,
        'manicure_services': manicure_services,
        'brow_services': brow_services,
        'henna_brow_services': henna_brow_services,
        'shape_tint_services': shape_tint_services, })

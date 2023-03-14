from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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


@login_required
def add_services(request):
    """
    Function to view add services page.
    The get request returns the add services form.
    The post request checks the form is valid,
    saves the form if valid,
    returns services page and displays
    the success message. If not valid, error message
    is displayed.
    """

    if request.method == "POST" and request.user.is_superuser:
        form = ServiceForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Request successful',
                extra_tags='successful_request')
            return redirect('services')
        else:
            messages.error(
                request,
                'Request unsuccessful - address errors',
                extra_tags='unsuccessful_request')
            return render(request, 'services/add_services.html', context)
    form = ServiceForm()
    context = {
        'form': form
    }
    return render(request, 'services/add_services.html', context)


@login_required
def edit_services(request, service_id):
    """
    Function to view edit services page.
    The get request returns the edit services page.
    The post request checks the form is valid,
    saves the form if valid,
    returns services page and displays
    the success message. If not valid, error message
    is displayed.
    """

    service = get_object_or_404(Service, id=service_id)
    if request.method == "POST" and request.user.is_superuser:
        form = ServiceForm(request.POST, instance=service)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Request successful',
                extra_tags='successful_request')
            return redirect('services')
        else:
            messages.error(
                request,
                'Request unsuccessful - address errors',
                extra_tags='unsuccessful_request')
            return render(request, 'services/edit_services.html', context)
    form = ServiceForm(instance=service)
    context = {
        'form': form
    }
    return render(request, 'services/edit_services.html', context)


@login_required
def delete_services(request, service_id):
    """
    Function to view delete services page.
    The get request returns the delete services page.
    The post request deletes the service,
    returns the services page and displays success
    message on the services page.
    """

    service = get_object_or_404(Service, id=service_id)
    if request.method == "POST" and request.user.is_superuser:
        service.delete()
        messages.success(
            request,
            'Request successful',
            extra_tags='successful_request')
        return redirect('services')
    context = {
        'service': service
    }
    return render(request, 'services/delete_services.html', context)
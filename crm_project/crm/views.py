# crm/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Guest
from .forms import GuestForm

def index(request):
    guests = Guest.objects.order_by('-date_time').all()
    total_guests = guests.count()
    total_members = guests.filter(member=True).count()
    total_bar = guests.filter(bar_or_restaurant='Bar').count()
    total_restaurant = guests.filter(bar_or_restaurant='Restaurant').count()

    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestForm()

    context = {
        'form': form,
        'guests': guests,
        'total_guests': total_guests,
        'total_members': total_members,
        'total_bar': total_bar,
        'total_restaurant': total_restaurant
    }
    return render(request, 'crm/index.html', context)

def delete_guest(request, guest_id):
    guest = get_object_or_404(Guest, id=guest_id)
    guest.is_deleted = True
    guest.deleted_at = timezone.now()
    guest.save()
    return redirect('index')

def revert_guest(request, guest_id):
    guest = get_object_or_404(Guest, id=guest_id)
    guest.is_deleted = False
    guest.deleted_at = None
    guest.save()
    return redirect('index')

def edit_guest(request, id):
    guest = Guest.objects.get(id=id)
    if request.method == 'POST':
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestForm(instance=guest)
    return render(request, 'crm/edit_guest.html', {'form': form})

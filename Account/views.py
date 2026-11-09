from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.utils import timezone
from .models import Truck, Driver, Trip, Incident, Payment
from .forms import TruckForm, DriverForm, TripForm, IncidentForm, PaymentForm

@login_required
def dashboard(request):
    trips = Trip.objects.all()
    context = {
        "truck_count": Truck.objects.count(),
        "driver_count": Driver.objects.count(),
        "trip_count": trips.count(),
        "total_charge": trips.aggregate(v=Sum("transport_charge"))["v"] or 0,
        "total_paid": trips.aggregate(v=Sum("amount_paid"))["v"] or 0,
        "outstanding": sum(t.balance for t in trips),
        "recent_trips": trips.order_by("-trip_date", "-id")[:5],
    }
    return render(request, "transport/dashboard.html", context)

@login_required
def truck_list(request):
    return render(request, "transport/truck_list.html", {"items": Truck.objects.all()})

@login_required
def truck_add(request):
    form = TruckForm(request.POST or None)
    if form.is_valid():
        form.save(); messages.success(request, "Truck saved successfully."); return redirect("truck_list")
    return render(request, "transport/form.html", {"form": form, "title": "Add Truck"})

@login_required
def truck_edit(request, pk):
    obj = get_object_or_404(Truck, pk=pk)
    form = TruckForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save(); messages.success(request, "Truck updated."); return redirect("truck_list")
    return render(request, "transport/form.html", {"form": form, "title": "Edit Truck"})

@login_required
def truck_delete(request, pk):
    obj = get_object_or_404(Truck, pk=pk)
    if request.method == "POST":
        obj.delete(); messages.success(request, "Truck deleted."); return redirect("truck_list")
    return render(request, "transport/confirm_delete.html", {"object": obj})

@login_required
def driver_list(request):
    return render(request, "transport/driver_list.html", {"items": Driver.objects.all()})

@login_required
def driver_add(request):
    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save(); messages.success(request, "Driver saved successfully."); return redirect("driver_list")
    return render(request, "transport/form.html", {"form": form, "title": "Add Driver"})

@login_required
def driver_edit(request, pk):
    obj = get_object_or_404(Driver, pk=pk)
    form = DriverForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save(); messages.success(request, "Driver updated."); return redirect("driver_list")
    return render(request, "transport/form.html", {"form": form, "title": "Edit Driver"})

@login_required
def driver_delete(request, pk):
    obj = get_object_or_404(Driver, pk=pk)
    if request.method == "POST":
        obj.delete(); messages.success(request, "Driver deleted."); return redirect("driver_list")
    return render(request, "transport/confirm_delete.html", {"object": obj})

@login_required
def trip_list(request):
    return render(request, "transport/trip_list.html", {"items": Trip.objects.select_related("truck", "driver").order_by("-trip_date")})

@login_required
def trip_add(request):
    form = TripForm(request.POST or None)
    if form.is_valid():
        form.save(); messages.success(request, "Transportation record saved."); return redirect("trip_list")
    return render(request, "transport/form.html", {"form": form, "title": "Add Transportation Record"})

@login_required
def trip_edit(request, pk):
    obj = get_object_or_404(Trip, pk=pk)
    form = TripForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save(); messages.success(request, "Record updated."); return redirect("trip_list")
    return render(request, "transport/form.html", {"form": form, "title": "Edit Transportation Record"})

@login_required
def trip_delete(request, pk):
    obj = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        obj.delete(); messages.success(request, "Record deleted."); return redirect("trip_list")
    return render(request, "transport/confirm_delete.html", {"object": obj})

@login_required
def incident_list(request):
    return render(request, "transport/incident_list.html", {"items": Incident.objects.select_related("trip").order_by("-date_reported")})

@login_required
def incident_add(request):
    form = IncidentForm(request.POST or None)
    if form.is_valid():
        form.save(); messages.success(request, "Incident recorded."); return redirect("incident_list")
    return render(request, "transport/form.html", {"form": form, "title": "Record Damage or Shortage"})

@login_required
def payment_list(request):
    return render(request, "transport/payment_list.html", {"items": Payment.objects.select_related("trip").order_by("-payment_date")})

@login_required
def payment_add(request):
    form = PaymentForm(request.POST or None)
    if form.is_valid():
        payment = form.save()
        payment.trip.amount_paid = (payment.trip.payments.aggregate(total=Sum("amount"))["total"] or 0)
        payment.trip.save(update_fields=["amount_paid"])
        messages.success(request, "Payment recorded."); return redirect("payment_list")
    return render(request, "transport/form.html", {"form": form, "title": "Record Payment"})

@login_required
def reports(request):
    trips = Trip.objects.select_related("truck", "driver").order_by("-trip_date")
    return render(request, "transport/reports.html", {
        "trips": trips,
        "total_charge": trips.aggregate(v=Sum("transport_charge"))["v"] or 0,
        "total_paid": trips.aggregate(v=Sum("amount_paid"))["v"] or 0,
        "outstanding": sum(t.balance for t in trips),
    })


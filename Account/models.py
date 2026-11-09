from django.db import models
from django.core.validators import MinValueValidator

class Truck(models.Model):
    plate_number = models.CharField(max_length=30, unique=True)
    truck_name = models.CharField(max_length=100)
    capacity = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=20, choices=[("Available", "Available"), ("On Trip", "On Trip"), ("Maintenance", "Maintenance")], default="Available")

    def __str__(self):
        return f"{self.plate_number} - {self.truck_name}"

class Driver(models.Model):
    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    license_number = models.CharField(max_length=50, unique=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.full_name

class Trip(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.PROTECT)
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT)
    goods = models.CharField(max_length=150)
    quantity = models.CharField(max_length=80, blank=True)
    origin = models.CharField(max_length=120)
    destination = models.CharField(max_length=120)
    trip_date = models.DateField()
    transport_charge = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    notes = models.TextField(blank=True)

    @property
    def balance(self):
        return self.transport_charge - self.amount_paid

    def __str__(self):
        return f"{self.goods}: {self.origin} to {self.destination}"

class Incident(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="incidents")
    incident_type = models.CharField(max_length=20, choices=[("Damage", "Damage"), ("Shortage", "Shortage")])
    description = models.TextField()
    quantity_affected = models.CharField(max_length=80, blank=True)
    date_reported = models.DateField()

    def __str__(self):
        return f"{self.incident_type} - Trip #{self.id}"

class Payment(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    payment_date = models.DateField()
    method = models.CharField(max_length=30, choices=[("Cash", "Cash"), ("Bank Transfer", "Bank Transfer"), ("Other", "Other")], default="Cash")
    reference = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Payment #{self.id} - {self.amount}"


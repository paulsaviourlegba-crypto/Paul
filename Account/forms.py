from django import forms
from .models import Truck, Driver, Trip, Incident, Payment

class DateInput(forms.DateInput):
    input_type = "date"

class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

class TruckForm(StyledModelForm):
    class Meta:
        model = Truck
        fields = "__all__"

class DriverForm(StyledModelForm):
    class Meta:
        model = Driver
        fields = "__all__"

class TripForm(StyledModelForm):
    class Meta:
        model = Trip
        fields = "__all__"
        widgets = {"trip_date": DateInput()}

class IncidentForm(StyledModelForm):
    class Meta:
        model = Incident
        fields = "__all__"
        widgets = {"date_reported": DateInput()}

class PaymentForm(StyledModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        widgets = {"payment_date": DateInput()}

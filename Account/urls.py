from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Account'

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("trucks/", views.truck_list, name="truck_list"),
    path("trucks/add/", views.truck_add, name="truck_add"),
    path("trucks/<int:pk>/edit/", views.truck_edit, name="truck_edit"),
    path("trucks/<int:pk>/delete/", views.truck_delete, name="truck_delete"),
    path("drivers/", views.driver_list, name="driver_list"),
    path("drivers/add/", views.driver_add, name="driver_add"),
    path("drivers/<int:pk>/edit/", views.driver_edit, name="driver_edit"),
    path("drivers/<int:pk>/delete/", views.driver_delete, name="driver_delete"),
    path("trips/", views.trip_list, name="trip_list"),
    path("trips/add/", views.trip_add, name="trip_add"),
    path("trips/<int:pk>/edit/", views.trip_edit, name="trip_edit"),
    path("trips/<int:pk>/delete/", views.trip_delete, name="trip_delete"),
    path("incidents/", views.incident_list, name="incident_list"),
    path("incidents/add/", views.incident_add, name="incident_add"),
    path("payments/", views.payment_list, name="payment_list"),
    path("payments/add/", views.payment_add, name="payment_add"),
    path("reports/", views.reports, name="reports"),
]

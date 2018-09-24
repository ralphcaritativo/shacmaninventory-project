from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inventory_dashboard, name = "inventory_dashboard"),
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.system_dashboard, name = "system_dashboard"),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.item_master, name = "item_master")
]

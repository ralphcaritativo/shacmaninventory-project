from django.urls import path
from . import views


urlpatterns = [
    path('', views.receiving_transaction_list, name = "receiving_transaction_list")
]

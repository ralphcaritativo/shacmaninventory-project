from django.urls import path
from . import views


urlpatterns = [
    path('', views.issuing_transaction_list, name = "issuing_transaction_list")
]

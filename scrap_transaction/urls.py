from django.urls import path
from . import views


urlpatterns = [
    path('', views.scrap_transaction_list, name = "scrap_transaction_list")
]

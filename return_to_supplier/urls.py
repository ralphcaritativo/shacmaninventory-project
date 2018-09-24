from django.urls import path
from . import views


urlpatterns = [
    path('', views.return_to_supplier_list, name = "return_to_supplier_list")
]

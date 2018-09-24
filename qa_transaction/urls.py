from django.urls import path
from . import views


urlpatterns = [
    path('', views.qa_transaction_list, name = "qa_transaction_list")
]

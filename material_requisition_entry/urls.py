from django.urls import path
from . import views


urlpatterns = [
    path('', views.material_requisition_entry_list, name = "material_requisition_entry_list")
]

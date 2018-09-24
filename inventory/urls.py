from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inventory_dashboard, name = "inventory_dashboard"),
    path('item_master/', views.item_master_list, name = "item_master_list"),
    path('receiving_transaction/', views.receiving_transaction_list, name = "receiving_transaction_list"),
    path('qa_transaction/', views.qa_transaction_list, name = "qa_transaction_list"),
    path('return_to_supplier/', views.return_to_supplier_list, name = "return_to_supplier_list"),
    path('material_requisition_entry/', views.material_requisition_entry_list, name = "material_requisition_entry_list"),
    path('issuing_transaction/', views.issuing_transaction_list, name = "issuing_transaction_list"),
    path('scrap_transaction/', views.scrap_transaction_list, name = "scrap_transaction_list"),
    path('inventory_maintenance/', views.inventory_maintenance, name = "inventory_maintenance"),
]

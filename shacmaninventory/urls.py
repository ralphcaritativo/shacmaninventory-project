from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("dashboard.urls")),
    path('inventory/', include("inventory.urls")),
    path('item_master/', include("item_master.urls")),
    path('receiving_transaction/', include("receiving_transaction.urls")),
    path('qa_transaction/', include("qa_transaction.urls")),
    path('return_to_supplier/', include("return_to_supplier.urls")),
    path('material_requisition_entry/', include("material_requisition_entry.urls")),
    path('issuing_transaction/', include("issuing_transaction.urls")),
    path('scrap_transaction/', include("scrap_transaction.urls")),
]

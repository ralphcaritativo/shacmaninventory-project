from django.shortcuts import render

# Inventory Dashboard
def inventory_dashboard(request):
    return render(request, 'inventory/inventory_dashboard.html')


# Item Master
def item_master_list(request):
    return render(request, 'inventory/item_master.html')

# !==================================================================================!


# Receiving Transaction
def receiving_transaction_list(request):
    return render(request, 'inventory/receiving_transaction_list.html')

# !==================================================================================!


# QA Transaction
def qa_transaction_list(request):
    return render(request, 'inventory/qa_transaction_list.html')

# !==================================================================================!


# Return to Supplier
def return_to_supplier_list(request):
    return render(request, 'inventory/return_to_supplier_list.html')

# !==================================================================================!


# Material Requisition Entry
def material_requisition_entry_list(request):
    return render(request, 'inventory/material_requisition_entry_list.html')

# !==================================================================================!


# Issuing transaction
def issuing_transaction_list(request):
    return render(request, 'inventory/issuing_transaction_list.html')

# !==================================================================================!



# Scrap Transaction
def scrap_transaction_list(request):
    return render(request, 'inventory/scrap_transaction_list.html')

# !==================================================================================!




# Inventory Maintenance
def inventory_maintenance(request):
    return render(request, 'inventory/inventory_maintenance.html')

# !==================================================================================!

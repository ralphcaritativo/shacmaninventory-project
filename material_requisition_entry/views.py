from django.shortcuts import render


def material_requisition_entry_list(request):
    return render(request, 'material_requisition_entry/material_requisition_entry_list.html')

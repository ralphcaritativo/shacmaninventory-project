from django.shortcuts import render


def return_to_supplier_list(request):
    return render(request, 'return_to_supplier/return_to_supplier_list.html')

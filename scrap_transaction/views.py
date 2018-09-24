from django.shortcuts import render


def scrap_transaction_list(request):
    return render(request, 'scrap_transaction/scrap_transaction_list.html')

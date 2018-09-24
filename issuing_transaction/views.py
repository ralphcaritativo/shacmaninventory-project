from django.shortcuts import render



def issuing_transaction_list(request):
    return render(request, 'issuing_transaction/issuing_transaction_list.html')

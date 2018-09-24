from django.shortcuts import render



def receiving_transaction_list(request):
    return render(request, 'receiving_transaction/receiving_transaction_list.html')

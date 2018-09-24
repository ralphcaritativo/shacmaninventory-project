from django.shortcuts import render


def qa_transaction_list(request):
    return render(request, 'qa_transaction/qa_transaction_list.html')

from django.shortcuts import render


def item_master(request):
    return render(request, 'item_master/item_master.html')

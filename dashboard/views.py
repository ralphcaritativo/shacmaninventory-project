from django.shortcuts import render


def system_dashboard(request):
    return render(request, 'dashboard/system_dashboard.html')

from django.shortcuts import render

# Create your views here.

def TimerView(request):
    return render(request, "portal/timer.html")
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def page404(request):
    return render(request,'status/404.html')

def page500(request):
    return render(request,'status/500.html')
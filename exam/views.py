from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(req):
    return render(req,'exam/index.html')

def school(request):
    return render(request, 'exam/school.html')

def office(request):
    return render(request, 'exam/office.html')

def center(request):
    return render(request, 'exam/center.html')
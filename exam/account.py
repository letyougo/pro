from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
# Create your views here.

from django.contrib import auth
from .models import School,Center,Office
from exam.models import Shortmsg
from django import forms
import requests
from django.http.response import HttpResponseRedirect
import random
def forget(request):
    return render(request,'account/forget.html')

def login(request):

    if request.method == 'GET':
        return render(request, 'account/login.html')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    # print(user,user.is_active)



    if user and user.is_active:
        u = auth.login(request, user)

        if School.objects.filter(user=user).exists():
            print('i am school')


        if Office.objects.filter(user=user).exists():
            print('i am office')

        if Center.objects.filter(user=user).exists():
            print('i am center')

        return HttpResponseRedirect(('/'))

        # if user.school:
        #     return HttpResponseRedirect('/school/')
        # elif user.office:
        #     return HttpResponseRedirect('/office/')
        # elif user.center:
        #     return HttpResponseRedirect('/center/')
        #     #

def make():
    return str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def sendcode(request):
    code =make()
    phone = request.GET.get('phone')
    requests.get('http://101.200.129.112:7788/send?phone='+phone+'&code='+code,)
    Shortmsg.objects.create(phone=phone,code=code)
    return HttpResponse(dict(phone=phone,code=code))

def changepwd(request):
    phone = request.GET.get('phone')
    code = request.GET.get('code')
    try:
        msg = Shortmsg.objects.get(phone=phone,code=code)


        username = request.POST.get()
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)
        # print(user,user.is_active)

        if user and user.is_active:
            u = auth.login(request, user)

            if School.objects.filter(user=user).exists():
                print('i am school')

            if Office.objects.filter(user=user).exists():
                print('i am office')

            if Center.objects.filter(user=user).exists():
                print('i am center')

            return HttpResponseRedirect(('/'))
    except:
        return JsonResponse(dict(
            error=True,
            msg="code error"
        ))
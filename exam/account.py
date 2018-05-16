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
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime,timedelta
def get_phone(user):
    return get_user(user).admin_phone

def get_user(user):
    try:
        is_center = user.center
    except:
        is_center = False

    try:
        is_office = user.office
    except:
        is_office = False

    try:
        is_school = user.school
    except:
        is_school = False

    if is_center:
        return is_center
    if is_office:
        return is_office
    if is_school:
        return is_school

def get_user_by_phone(phone):
    try:
        center = Center.objects.get(admin_phone=phone)
        return center.user
    except:
        pass

    try:
        office = Office.objects.get(admin_phone=phone)
        return office.user
    except:
        pass

    try:
        school = School.objects.get(admin_phone=phone)
        return school.user
    except:
        pass

def forget(request):
    return render(request,'account/forget.html')

def login(request):

    if request.method == 'GET':
        return render(request, 'account/login.html')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    phone = request.POST.get('phone')
    code = request.POST.get('code')
    smg = Shortmsg.objects.filter(phone=phone).last()
    t1 = datetime.now()
    t2= smg.create_time
    delta = timedelta(minutes=5)
    expired = t1 - delta > t2

    user = auth.authenticate(username=username, password=password)


    error = ''

    if user and user.is_active:

        if get_phone(user) == phone:
            if code == smg.code:
                if not expired:
                    u = auth.login(request, user)
                    return HttpResponseRedirect(('/'))
                else:
                    error='验证码过期了'
            else:
                error='验证码错误'
        else:
            error='绑定的手机号错误'

    else:
        error='密码错误'

    return render(request,'status/500.html',dict(error=error))


def make():
    return str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def sendcode(request):
    code =make()
    phone = request.GET.get('phone')
    requests.get('http:/localhost:7788/send?phone='+phone+'&code='+code,)
    Shortmsg.objects.create(phone=phone,code=code)
    return HttpResponse(dict(phone=phone,code=code))

def changepwd(request):
    phone = request.POST.get('phone')
    code = request.POST.get('code')
    pwd = request.POST.get('pwd')

    msg = Shortmsg.objects.filter(phone=phone).last()

    if msg.code == code:

        user = get_user_by_phone(phone)
        user.password = make_password(pwd)
        user.save()
        auth.login(request, user)
        return HttpResponseRedirect(('/'))


def changephone(request):
    phone = request.GET.get('phone')
    new_phone = request.GET.get('new_phone')
    code = request.GET.get('code')
    role = request.GET.get('role')
    try:
        msg = Shortmsg.objects.filter(phone=phone).last()

        if msg.code == code:
            if role == 'center':
                center = request.user.center
                center.admin_phone = new_phone

                center.save()
            if role == 'office':
                office = request.user.office
                office.admin_phone = new_phone

                office.save()
            if role == 'school':
                school = request.user.school
                school.admin_phone =new_phone

                school.save()



            return JsonResponse(dict(error=False))
        else:
            return JsonResponse(dict(error=True,msg='code error'))

    except:
        return JsonResponse(dict(error=True, msg='code error'))


def setphone(request):
    phone = request.GET.get('phone')

    code = request.GET.get('code')
    role = request.GET.get('role')
    try:
        msg = Shortmsg.objects.filter(phone=phone).last()

        if msg.code == code:
            if role == 'center':
                center = request.user.center
                center.admin_phone = phone

                center.save()
            if role == 'office':
                office = request.user.office
                office.admin_phone = phone

                office.save()
            if role == 'school':
                school = request.user.school
                school.admin_phone =phone
                school.save()

            return JsonResponse(dict(error=False))
        else:
            return JsonResponse(dict(error=True,msg='code error'))

    except:
        return JsonResponse(dict(error=True, msg='code error'))
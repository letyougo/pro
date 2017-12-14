from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

import requests
import os
from pro.settings import BASE_DIR
import base64
import xlrd
@login_required
def index(req):
    return render(req,'exam/index.html')

def school(request):
    school = request.user.school
    return render(request, 'exam/school.html')

def office(request):
    office = request.user.office
    return render(request, 'exam/office.html')

def center(request):
    center = request.user.center
    return render(request, 'exam/center.html')

def upload(request):
    file = request.FILES.get('file')
    print(file,file.name)

    destination = open(os.path.join(os.path.join(BASE_DIR, "static",'upload','teacher'), file.name), 'wb+')
    for chunk in file.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()

    pic = open(os.path.join(BASE_DIR, "static", 'upload', 'teacher',file.name),'rb')
    print(os.path.join(BASE_DIR, "static", 'upload', 'teacher',file.name))
    ls_f = base64.b64encode(pic.read())

    pic.close()
    data = dict(
        api_key='tmD-RlJfiw4IdBC6TV5M1pAhn7y2elj2',
        api_secret='2WrohOvUZGtbzazkCg1Bw7wKJ7jhjn4Q',
        image_base64=ls_f
    )

    r = requests.post("https://api-cn.faceplusplus.com/cardpp/v1/ocridcard", data=data)
    print(r.json())

    return JsonResponse(r.json())

def upload2(request):
    file = request.FILES.get('file')
    print(file.get_path_info())
    data = xlrd.open_workbook(file)
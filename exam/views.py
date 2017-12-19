from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.core.paginator import Paginator
from pro.settings import PAGE_NUM,PAGE_SIZE
from .models import Teacherexam,Schoolexam,School,Office,Exam
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


    destination = open(os.path.join(os.path.join(BASE_DIR, "static",'upload','teacher'), file.name), 'wb+')
    for chunk in file.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()

    pic = open(os.path.join(BASE_DIR, "static", 'upload', 'teacher',file.name),'rb')

    ls_f = base64.b64encode(pic.read())

    pic.close()
    data = dict(
        api_key='tmD-RlJfiw4IdBC6TV5M1pAhn7y2elj2',
        api_secret='2WrohOvUZGtbzazkCg1Bw7wKJ7jhjn4Q',
        image_base64=ls_f
    )

    r = requests.post("https://api-cn.faceplusplus.com/cardpp/v1/ocridcard", data=data)


    return JsonResponse(r.json())


def excel(request):

    start = date_parse(request.GET['start'])
    end = date_parse(request.GET['end'])
    page_size = int(request.GET.get('page_size', PAGE_SIZE))
    page_num = int(request.GET.get('page_num', PAGE_NUM))
    if  'school_id' in request.GET:
        school = School.objects.get(id=int(request.GET['school_id']))
        query = Teacherexam.objects.filter(schoolexam__school=school,schoolexam__exam__time__range=[start,end])
        exam = Exam.objects.filter(time__range=[start, end])
    elif 'office_id' in request.GET:
        office = Office.objects.get(id=request.GET['office_id'])
        exam = Exam.objects.filter(office=office,time__range=[start, end])
        query = Teacherexam.objects.filter(schoolexam__exam__office=office,schoolexam__exam__time__range=[start,end])
    else:
        exam = Exam.objects.filter( time__range=[start, end])
        query = Teacherexam.objects.filter(schoolexam__exam__time__range=[start,end])

    paginator = Paginator(query, page_size)
    page = paginator.page(page_num)



    return JsonResponse(
        dict(
            page=dict(
                page_size=page_size,
                page_num=page_num,
                total=len(query)
            ),
            list=[t.to_obj() for t in page],
            exam= [e.to_obj() for e in exam]
        )
    )

    return JsonResponse(
        [item.to_obj() for item in query],
        safe=False
    )

import datetime
def date_parse(time):
    return datetime.datetime.strptime(time, '%Y-%m-%d').date()

def upload2(request):
    file = request.FILES.get('file')

    data = xlrd.open_workbook(file)
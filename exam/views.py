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
from pro.settings import DEBUG

@login_required
def index(req):

    if DEBUG:
        return render(req,'exam_dev/index.html')
    return render(req,'exam/index.html')

def school(request):
    school = request.user.school
    # if DEBUG:
    #     return render(request,'exam_dev/school.html')
    return render(request, 'exam/school.html')

def office(request):
    office = request.user.office
    if DEBUG:
        return render(request,'exam_dev/office.html')
    return render(request, 'exam/office.html')

def center(request):
    center = request.user.center
    if DEBUG:
        return render(request,'exam_dev/center.html')
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
    client = ''
    if  'school_id' in request.GET:
        school = School.objects.get(id=int(request.GET['school_id']))
        query = Teacherexam.objects.filter(schoolexam__school=school,schoolexam__exam__time__range=[start,end])
        exam = Exam.objects.filter(time__range=[start, end])
        client = 'school'
    elif 'office_id' in request.GET:
        office = Office.objects.get(id=request.GET['office_id'])
        exam = Exam.objects.filter(office=office,time__range=[start, end])
        query = Teacherexam.objects.filter(schoolexam__exam__office=office,schoolexam__exam__time__range=[start,end])
        client = 'office'
    else:
        exam = Exam.objects.filter( time__range=[start, end])
        query = Teacherexam.objects.filter(schoolexam__exam__time__range=[start,end])
        client = 'center'

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
import xlwt
from django.contrib.auth.models import User
def date_parse(time):
    return datetime.datetime.strptime(time, '%Y-%m-%d').date()

def upload2(request):
    file = request.FILES.get('file')

    data = xlrd.open_workbook(file)


def _find(list,fn):
    for item in list:
        if fn(item):
            return item

    return False

def data_export(request):
    start = date_parse(request.GET['start'])
    end = date_parse(request.GET['end'])

    client = dict(
        year=str(start.year),
        month=str(start.month)
    )

    if 'school_id' in request.GET:
        school = School.objects.get(id=int(request.GET['school_id']))
        query = Teacherexam.objects.filter(schoolexam__school=school, schoolexam__exam__time__range=[start, end])
        exam = Exam.objects.filter(time__range=[start, end])
        client['type'] = 'school'
    elif 'office_id' in request.GET:
        office = Office.objects.get(id=request.GET['office_id'])
        exam = Exam.objects.filter(office=office, time__range=[start, end])
        query = Teacherexam.objects.filter(schoolexam__exam__office=office, schoolexam__exam__time__range=[start, end])
        client['type']= 'office'
    else:
        exam = Exam.objects.filter(time__range=[start, end])
        query = Teacherexam.objects.filter(schoolexam__exam__time__range=[start, end])
        client['type'] = 'center'

    list = [t.to_obj() for t in query]
    res = {}
    exam_obj = {}
    header = []
    for e in exam:
        e1 = e.to_obj()
        desc = e1['desc']
        exam_obj[desc] = 0


    for item in list:

        for e in exam_obj:
            item[e] = 0

    for item in list:
        item[item['desc']] = item['total']

    for item in list:
        _id ='teacher_' + str(item['teacher']['id'])

        if _id not in res:
            res[_id] = item

        desc = item['desc']
        res[_id][desc] = item['total']

    result = []
    i=0
    for r in res:
        i=i+1
        obj = {}
        item = res[r]
        num = 0
        for k in exam_obj:
            obj[k] = item[k]
            num+=obj[k]
        obj['序号'] = i
        obj['身份证'] = item['teacher']['idcard']
        obj['银行卡号'] = item['teacher']['bankcard']
        obj['姓名'] = item['teacher']['name']
        obj['所属学校'] = item['teacher']['school_name']
        obj['总计'] = num
        obj['应缴税金'] = ''
        obj['实发金额'] = ''
        obj['本人签字'] = ''
        result.append(obj)
    header.append('序号')
    header.append('姓名')
    header.append('所属学校')
    header.append('身份证')
    header.append('银行卡号')
    for e in exam_obj:
        header.append(e)
    header.append('总计')
    header.append('应缴税金')
    header.append('实发金额')
    header.append('本人签字')

    return export_users_csv(header,result,client)



def export_users_csv(header,data,client):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="total.xls"'

    title = client['year']+ '年'+client['month']+'务费合并计税发放表'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(title)

    # Sheet header, first row



    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER


    font0 =xlwt.Font()

    font0.height = 300

    columns = header

    font1 = xlwt.Font()
    font1.bold = True

    style = xlwt.XFStyle()
    style.alignment = alignment
    style.font = font0
    ws.write_merge(0, 1, 0, len(columns)-1, title,style)
    ws.write_merge(2,3,0,len(columns)-1,'单位签字(公章)')
    # ws.write(1, 1, 2)

    style = xlwt.XFStyle()
    style.alignment = alignment
    style.font = font1

    row_num = 4
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], style)

    # Sheet body, remaining rows
    style = xlwt.XFStyle()

    for row in data:
        row_num += 1

        for col_num in range(len(header)):
            ws.write(row_num, col_num, row[header[col_num]], style)



    ws.write_merge(row_num+1, row_num+1, 0, 3, '合计',style)
    ws.write_merge(row_num + 2, row_num + 2, 0, 2, '经手人', style)
    ws.write_merge(row_num + 2, row_num + 2, 3, 6, '主管领导签字', style)
    ws.write_merge(row_num + 2, row_num + 2, 7, 11, '日期', style)
    # ws.write_merge(2,3,0,len(columns)-1,'单位签字(公章)')
    wb.save(response)
    return response

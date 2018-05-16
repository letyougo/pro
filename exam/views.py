from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.core.paginator import Paginator
from pro.settings import PAGE_NUM,PAGE_SIZE
from .models import Teacherexam,Schoolexam,School,Office,Exam,Config,Teacher
import requests
import os
from pro.settings import BASE_DIR
import base64
import xlrd
from pro.settings import DEBUG

@login_required
def index(req):

    #
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
    # if DEBUG:
    #     return render(request,'exam_dev/office.html')
    return render(request, 'exam/office.html')

def center(request):
    center = request.user.center
    # if DEBUG:
    #     return render(request,'exam_dev/center.html')
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

def excel(request):

   

    return JsonResponse(
        get_data(request),
        safe=False
    )

def office_template(request):


    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="office-template.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')
    header = ['学校名', '监考费']

    row_num = 0
    for i in range(len(header)):
        ws.write(row_num, i, header[i])
    row_num = row_num + 1


    exam = Exam.objects.get(id=int(request.GET['id']))
    list = Schoolexam.objects.filter(exam=exam)
    for item in list:
        ws.write(row_num,0,item.school.name)
        ws.write(row_num, 1, item.total)
        row_num = row_num+1

    wb.save(response)
    return response


def teacherexport(request):
    id = request.GET['school_id']
    school = School.objects.get(id=int(id))
   
    teacher = [t.to_excel() for t in Teacher.objects.filter(school=school)]

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="teacher.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(school.name)
    header = ['姓名','电话','身份证号','银行卡号','银行信息']
    row_num= 0 
    for i in range(len(header)):
        ws.write(row_num, i, header[i])
    row_num=row_num+1  
    for row in teacher:
        for col_num in range(len(header)):
            ws.write(row_num, col_num, row[header[col_num]])
        row_num += 1

    ws.col(2).width = 256*20    
    wb.save(response)
    return response


def jssq(request):
    start = date_parse(request.GET['start'])
    end = date_parse(request.GET['end'])
    query = Teacherexam.objects.filter(schoolexam__exam__time__range=[start, end])
    exam = Exam.objects.filter(time__range=[start, end])


    list = [t.to_obj() for t in query]


    base = Config.objects.get(key="base")
    rate = Config.objects.get(key="rate")
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
        _id = 'teacher_' + str(item['teacher']['id'])
        desc = item['desc']
        if _id not in res:
            res[_id] = item
            res[_id][desc] = item['total']
        else:
            res[_id][desc] = res[_id][desc] + item['total']







    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="total.xls"'

    title =  str(start)+'-'+str(end)+ '金税三期表'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(title)

    # Sheet header, first row
    header = ['姓名','证件类型','证件号码','所得期间起','所得期间止','收入额','免税所得','基本养老保险费','基本医疗保险费',
              '失业保险费用','住房公积金','允许扣除的税费','其他','税前扣除项目合计','减除费用','实际捐赠额','允许列支的捐赠比例','准予扣除捐赠额','扣除及减除项目合计','应纳税所得额','税率','应纳税额','减免税额','应扣缴税额']

    row_num=0
    for i in range(len(header)):
        ws.write(row_num, i, header[i])
    row_num = row_num + 1

    for key in res:

        item=res[key]

        ws.write(row_num, 0, item['teacher']['name'])
        ws.write(row_num, 1, '身份证')
        ws.write(row_num, 2, item['teacher']['idcard'])
        ws.write(row_num, 3, str(start))
        ws.write(row_num, 4, str(end))

        shui = (item['total'] - float(base.value)) * float(rate.value)
        shui = 0 if shui < 0 else shui

        ws.write(row_num, 5, item['total'])
        # ws.write(row_num,6,item['total'])
        ws.write(row_num, 14, 800)
        ws.write(row_num, 18, 800)
        ws.write(row_num, 19, 0 if item['total']-800 < 0 else item['total']-800)
        ws.write(row_num, 20, '20%')
        ws.write(row_num, 21, shui*0.2)
        ws.write(row_num, 23, shui * 0.2)
        row_num = row_num + 1
    ws.col(2).width = 256 * 40
    wb.save(response)
    return response



def data_export(request):
    obj = get_data(request)
    # return obj
    return export_users_csv(obj['header'],obj['result'],obj['client'])

def get_data(request):
    start = date_parse(request.GET['start'])
    end = date_parse(request.GET['end'])

    client = dict(
        year=str(start.year),
        month=str(start.month)
    )
    query=[]
    exam=[]


    if 'office_id' in request.GET:
        office = Office.objects.get(id=request.GET['office_id'])
        exam = Exam.objects.filter(office=office, time__range=[start, end])
        if int(request.GET['school_id'])==0:
            query = Teacherexam.objects.filter(schoolexam__exam__office=office, schoolexam__exam__time__range=[start, end])
        else:
            school = School.objects.get(id=int(request.GET['school_id']))
            query = Teacherexam.objects.filter(schoolexam__exam__office=office, teacher__school=school,schoolexam__exam__time__range=[start, end])
    else:
        if int(request.GET['school_id'])==0:
                query = Teacherexam.objects.filter(schoolexam__exam__time__range=[start,end])
        else:
            school = School.objects.get(id=int(request.GET['school_id']))
            query = Teacherexam.objects.filter(teacher__school=school,schoolexam__exam__time__range=[start, end])
        exam = Exam.objects.filter(time__range=[start, end])
        client['type'] = 'school'

 



    list = [t.to_obj() for t in query]
 
    base = Config.objects.get(key="base")
    rate = Config.objects.get(key="rate")
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
        desc = item['desc']
        if _id not in res:
            res[_id] = item
            res[_id][desc] = item['total']
        else:
            res[_id][desc] =res[_id][desc]+ item['total']

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
 
        shui =  (num - float(base.value)) * float(rate.value)
        shui = 0 if shui<0 else shui
        obj['序号'] = i
        obj['身份证'] = item['teacher']['idcard']
        obj['银行卡号'] = item['teacher']['bankcard']
        obj['姓名'] = item['teacher']['name']
        obj['所属学校'] = item['teacher']['school_name']
        obj['应发金额'] = num
        obj['应缴税金'] = shui 
        obj['实发金额'] = float(num) - float(shui)
        obj['本人签字'] = ''
        result.append(obj)
    header.append('序号')
    header.append('姓名')
    header.append('所属学校')
    header.append('身份证')
    header.append('银行卡号')
    for e in exam_obj:
        header.append(e)
    header.append('应发金额')
    header.append('应缴税金')
    header.append('实发金额')
    header.append('本人签字')

    # return  JsonResponse(
    #     dict(
    #         header=header,
    #         result=result,
    #         client=client
    #     ),safe=False
    #
    # )
 
    return dict(
        header=header,
        result=result,
        client=client
    )
   



def export_users_csv(header,data,client):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="total.xls"'

    title = client['year']+ '年'+client['month']+'月劳务费合并计税发放表'



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
    row_num = row_num+1

    for row in data:
 

        for col_num in range(len(header)):
            ws.write(row_num, col_num, row[header[col_num]], style)
        row_num += 1


    ws.write(row_num, 0,  '合计',style)
    for i in range(5,len(header)-1):
        en = chr(ord('A')+i)
        fm = ' SUM('+en+'6'+':'+en+str(5+len(data))+')'
        ws.write(row_num, i,xlwt.Formula(fm))


    ws.write_merge(row_num + 1, row_num + 1, 0, 2, '经手人', style)
    ws.write_merge(row_num + 1, row_num + 1, 3, 6, '主管领导签字', style)
    ws.write_merge(row_num + 1, row_num + 1, 7, 11, '日期', style)
    ws.col(2).width = 256*40
    ws.col(3).width = 256*40
    wb.save(response)
    return response

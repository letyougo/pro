from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from django.http import JsonResponse,HttpResponse
from exam.models import Teacher,School,Exam
from django.views import View
from pro.settings import PAGE_SIZE,PAGE_NUM
from django.core.paginator import Paginator
import json
import simplejson
from exam.api.base import Base 


class teacher2(View):
    def get(self,request):

        page_size = int(request.GET.get('page_size',PAGE_SIZE))
        page_num = int(request.GET.get('page_num',PAGE_NUM))

        school = School.objects.get(id=int(request.GET['school_id']))
        teacher = Teacher.objects.filter(school=school)
        paginator = Paginator(teacher, page_size)
        pa = paginator.page(page_num)
        return JsonResponse(
            dict(
                page=dict(
                    page_size=page_size,
                    page_num=page_num,
                    total=len(teacher)
                ),
                list=[t.to_obj() for t in pa]
            )
        )

    def post(self,request):

        body = simplejson.loads(request.body)
        list = body['list']
        school_id = int(body['school_id'])
    
        idcards = []
        names = []
        bulk_teacher = []
        update = []
        for item in list:
            if item['idcard'] not in idcards:
               
                if not Teacher.objects.filter(idcard=item['idcard']).exists():
                    t = Teacher(
                        name=item['name'],
                        idcard=item['idcard'],
                        phone=  item['phone'] if 'phone' in item else '',
                        bankcard=item['bankcard']  if 'bankcard' in item else '',
                        bankinfo=item['bankinfo'] if 'bankinfo' in item else '',
                        school=School.objects.get(id=school_id)
                    )
                    idcards.append(item['idcard'])
                    bulk_teacher.append(t)
                    names.append(item['name'])
                else:
                    teacher = Teacher.objects.get(idcard=item['idcard'])
                    teacher.name = item['name']
                    teacher.phone = item['phone'] 
                    teacher.bankcard=item['bankcard'] 
                    teacher.bankinfo=item['bankinfo']
                    update.append(item['name'])
                    teacher.save()
            else:
                names.append(item['name'])
        
        Teacher.objects.bulk_create(bulk_teacher)
        return JsonResponse(dict(error=False,create=len(bulk_teacher),repeat=names,update=update))









def create2(request):
    pass

class TeacherResource(Base):
    # Controls what data is included in the serialized output.


    school_preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
    })
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
        'phone': 'phone',
        'idcard': 'idcard',
        'bankcard': 'bankcard',
        'bankinfo':'bankinfo',
        'school_id':'school.id',
        'create_time':'create_time',
        'school_name':'school.name'
    })

    def is_authenticated(self):

        return True


    # GET /
    def list(self):
        # if 'exam_time' in self.request.GET:
        #     school = School.objects.get(id=int(self.request.GET['school_id']))
        #     exam = Exam.objects.get(id=int(self.request.GET['exclude_exam_id']))
        #     return Teacher.objects.filter(school=school, name__contains=self.request.GET.get('search', '')).exclude(teacherexam__schoolexam__exam=exam)

        if 'school_id' in self.request.GET:
            school = School.objects.get(id=int(self.request.GET['school_id']))
            return Teacher.objects.filter(school=school,name__contains=self.request.GET.get('search',''))

        return Teacher.objects.filter(name__contains=self.request.GET.get('name',''),idcard__contains=self.request.GET.get('idcard',''))

    # GET /pk/
    def detail(self, pk):
        return Teacher.objects.get(id=pk)

    # POST /
    def create(self):

        return Teacher.objects.create(
            name=self.data['name'],
            phone=self.data['phone'],
            idcard=self.data['idcard'],
            bankcard=self.data['bankcard'],
            bankinfo=self.data['bankinfo'],
            school=self.request.user.school
        )

    # PUT /pk/
    def update(self, pk):
        try:
            post = Teacher.objects.get(id=pk)
        except Teacher.DoesNotExist:
            post = Teacher()

        post.name = self.data['name']
        post.phone = self.data['phone']
        post.idcard = self.data['idcard']
        post.bankcard = self.data['bankcard']
        post.bankinfo = self.data['bankinfo']

        post.save()
        return post



    # DELETE /pk/
    def delete(self, pk):
        Teacher.objects.get(id=pk).delete()
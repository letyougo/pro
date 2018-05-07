from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from exam.models import Teacher,School,Schoolexam,Exam,Teacherexam
from exam.api.base import Base 
from django.db.models import Avg,Max,Min,Count
from django.http import JsonResponse
from django.db.models import Sum
import simplejson
from django.views import View
class schoolexam2(View):


    def post(self, request):

        body = simplejson.loads(request.body)
        list = body['list']
        exam = Exam.objects.get(id=int(body['exam_id']))

        create = []
        update = []
        error=[]

        for item in list:
            if School.objects.filter(name=item['name']).exists():
                if Schoolexam.objects.filter(exam=exam,school__name=item['name']).exists():
                    schoolexam = Schoolexam.objects.get(exam=exam,school__name=item['name'])
                    schoolexam.total = item['total']
                    schoolexam.save()
                    item['status'] = '已更新'
                else:
                    s = Schoolexam(
                        school=School.objects.get(name=item['name']),
                        total=item['total'],
                        exam=exam,
                        status='uncheck',
                        lock2=False
                    )
                    create.append(s)
                    item['status'] = '已增加'
            else:
                item['status'] = "不存在该学校"


        Schoolexam.objects.bulk_create(create)
        return JsonResponse(dict(list=list))


def money(request):
    id = int(request.GET['exam_id'])
    exam = Exam.objects.get(id=id)
    query =Schoolexam.objects.filter(exam=exam).aggregate(Sum('total'))
    return JsonResponse(dict(
        spend=query['total__sum'],
        total=int(exam.total),
        exam_id=int(id)
    ))

class SchoolExamResource(Base):
    # Controls what data is included in the serialized output.


    exam_preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'time',
        'total':'total',
        'desc':'desc'
    })

    teacher_preparer = FieldsPreparer(fields={
        'id':'id',

    })
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'exam_id':'exam.id',
        'exam_time':'exam.time',
        'exam_desc':'exam.desc',
        'exam_total':'exam.total',

        "school_id":'school.id',
        'school_name':'school.name',

        'total':'total',
        'status':'status',
        'lock2':'lock2'
    })

    def is_authenticated(self):

        return True


    # GET /
    def list(self):


        if 'school_id' in self.request.GET:
            id = int(self.request.GET['school_id'])

            school = School.objects.get(id=id)
            return Schoolexam.objects.filter(school=school)

        if 'exam_id' in self.request.GET:
            id = int(self.request.GET['exam_id'])
            exam = Exam.objects.get(id=id)

            return Schoolexam.objects.filter(exam=exam,school__name__contains=self.request.GET.get('search',''))

        return Schoolexam.objects.all()

    # GET /pk/
    def detail(self, pk):
        return Schoolexam.objects.get(id=pk)

    # POST /
    def create(self):
        exam = Exam.objects.get(id=int(self.data['exam_id']))
        if exam.lock:
            return
        return Schoolexam.objects.create(
            exam=Exam.objects.get(id=int(self.data['exam_id'])),
            school = School.objects.get(id=int(self.data['school_id'])),
            total = self.data['total']
        )

    # PUT /pk/
    def update(self, pk):
        schoolexam = Schoolexam.objects.get(id=pk)
        exam = schoolexam.exam
        if exam.lock:
            return schoolexam

        schoolexam.total = self.data['total'] if 'total' in self.data else schoolexam.total
        schoolexam.lock2 = self.data['lock2'] if 'lock2' in self.data else schoolexam.lock2
        schoolexam.save()
        return schoolexam

    # DELETE /pk/
    def delete(self, pk):
        schoolexam = Schoolexam.objects.get(id=pk)
        exam = schoolexam.exam
        if exam.lock:
            return schoolexam

        return Schoolexam.objects.get(id=pk).delete()
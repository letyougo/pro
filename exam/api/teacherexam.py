from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from exam.models import Teacher,School,Teacherexam,Schoolexam
from exam.api.base import Base 
from django.http import JsonResponse
from django.db.models import Sum
def money2(request):
    id = int(request.GET['schoolexam_id'])
    schoolexam = Schoolexam.objects.get(id=int(request.GET['schoolexam_id']))
    query = Teacherexam.objects.filter(schoolexam=schoolexam).aggregate(Sum('total'))
    return JsonResponse(dict(
        spend=query['total__sum'],
        school_total=int(schoolexam.total),
        exam_id=int(id)
    ))

class TeacherExamResource(Base):
    # Controls what data is included in the serialized output.


    teacher_preparer = FieldsPreparer(fields={
        'id': 'id',

    })
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'exam_total':'schoolexam.exam.total',
        'exam_id':'schoolexam.exam.id',
        'exam_desc':'schoolexam.exam.desc',
        'exam_time':'schoolexam.exam.time',
        'school_exam_id': 'schoolexam.id',
        'school_exam_total': 'schoolexam.total',
        'school_name':'schoolexam.school.name',
        'teacher_total':'total',
        'teacher_id':'teacher.id',
        'teacher_name':'teacher.name',
        'teacher_in_school_id':'teacher.school.id',
        'teacher_in_school_name':'teacher.school.name',
        'lock2':'schoolexam.lock2'
        # 'month_total':'month_total'
        
    })

    def is_authenticated(self):

        return True


    # GET /
    def list(self):
        # user_id = self.request.user.id
        if 'schoolexam_id' in self.request.GET:
            schoolexam = Schoolexam.objects.get(id= int(self.request.GET['schoolexam_id']))
            return Teacherexam.objects.filter(schoolexam=schoolexam)
        if 'teacher_id' in self.request.GET:
            teacher = Teacher.objects.get(id=int(self.request.GET['teacher_id']))
            if 'start' in self.request.GET and 'end' in self.request.GET:

                return Teacherexam.objects.filter(teacher=teacher,schoolexam__exam__time__range=[self.request.GET['start'],self.request.GET['end']])
            else:
                return Teacherexam.objects.filter(teacher=teacher)


        return Teacherexam.objects.all()


    # GET /pk/
    def detail(self, pk):
        return Teacher.objects.get(id=pk)

    # POST /
    def create(self):


        if 'school_id' in self.data:
            teacher = Teacher.objects.get(
                school=School.objects.get(id=int(self.data['school_id'])),
                name=self.data['name']
            )
        else:
            teacher = Teacher.objects.get(id=int(self.data['teacher']))
        schoolexam = Schoolexam.objects.get(id=int(self.data['school_exam']))

        if schoolexam.lock2:
            return

        total = self.data['total']
        print('total')
        (teacherexam,bool) = Teacherexam.objects.get_or_create(
            teacher=teacher,
            schoolexam=schoolexam
        )

        teacherexam.total=total
        teacherexam.save()
        return teacherexam


    # PUT /pk/
    def update(self, pk):

        teacherexam = Teacherexam.objects.get(id=pk)
        schoolexam = teacherexam.schoolexam
        if schoolexam.lock2:
            return teacherexam
        teacherexam.total = self.data['teacher_total']
        teacherexam.save()
        return teacherexam



    # DELETE /pk/
    def delete(self, pk):
        print(pk,'delete ')
        teacherexam = Teacherexam.objects.get(id=int(pk))
        schoolexam = teacherexam.schoolexam
        if schoolexam.lock2:
            return teacherexam
        teacherexam.delete()

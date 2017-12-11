from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from exam.models import Teacher,School,Teacherexam,Schoolexam


class TeacherExamResource(DjangoResource):
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

        'teacher_total':'total',
        'teacher_id':'teacher.id',
        'teacher_name':'teacher.name',
        'teacher_in_school_id':'teacher.school.id',
        'teacher_in_school_name':'teacher.school.name'
    })

    def is_authenticated(self):

        return True
        # print(self.request.user.is_authenticated(),'-=----')
        # return self.request.user.is_authenticated()

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
        print(self.data,'---')
        teacher = Teacher.objects.get(id=int(self.data['teacher']))
        schoolexam = Schoolexam.objects.get(id=int(self.data['school_exam']))
        total = self.data['total']
        return Teacherexam.objects.create(
            teacher=teacher,
            schoolexam=schoolexam,
            total=total
        )

    # PUT /pk/
    def update(self, pk):
        print('hello ',pk)
        try:
            post = Teacherexam.objects.get(id=pk)
        except Teacher.DoesNotExist:
            post = Teacher()


        post.total = self.data['teacher_total']

        #
        post.save()
        return post



    # DELETE /pk/
    def delete(self, pk):
        Teacherexam.objects.get(id=pk).delete()
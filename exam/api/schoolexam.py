from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from exam.models import Teacher,School,Schoolexam,Exam


class SchoolExamResource(DjangoResource):
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

        'total':'total'
    })

    def is_authenticated(self):

        return True


    # GET /
    def list(self):


        if 'school_id' in self.request.GET:
            id = int(self.request.GET['school_id'][0])

            school = School.objects.get(id=id)
            return Schoolexam.objects.filter(school=school)

        if 'exam_id' in self.request.GET:
            id = int(self.request.GET['exam_id'][0])
            exam = Exam.objects.get(id=id)

            return Schoolexam.objects.filter(exam=exam)

        return Schoolexam.objects.all()


    # GET /pk/
    def detail(self, pk):
        return Schoolexam.objects.get(id=pk)

    # POST /
    def create(self):



        return Schoolexam.objects.create(
            exam=Exam.objects.get(id=int(self.data['exam_id'])),
            school = School.objects.get(id=int(self.data['school_id'])),
            total = self.data['total']
        )

    # PUT /pk/
    def update(self, pk):
        try:
            schoolexam = Schoolexam.objects.get(id=pk)
        except Schoolexam.DoesNotExist:
            schoolexam = Schoolexam()

        schoolexam.total = self.data['total']
        schoolexam.save()
        return schoolexam



    # DELETE /pk/
    def delete(self, pk):
        Schoolexam.objects.get(id=pk).delete()
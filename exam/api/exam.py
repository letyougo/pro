from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from exam.models import Teacher,School,Exam,Office


class ExamResource(DjangoResource):
    # Controls what data is included in the serialized output.


    school_preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
    })
    preparer = FieldsPreparer(fields={
        'id': 'id',
        # 'time':'time',
        'total':'total',
        'desc':'desc'
        # 'name': 'name',
        # 'phone': 'phone',
        # 'idcard': 'idcard',
        # 'bankcard': 'bankcard',
        # 'bankinfo':'bankinfo',
        # 'school_id':'school.id'
    })

    def is_authenticated(self):

        return True
        # print(self.request.user.is_authenticated(),'-=----')
        # return self.request.user.is_authenticated()

    # GET /
    def list(self):
        print(self.request.GET)
        office = Office.objects.get(id=int(self.request.GET['office_id']))
        return Exam.objects.filter(office=office)



    # GET /pk/
    def detail(self, pk):
        return Exam.objects.get(id=pk)

    # POST /
    def create(self):
        office = Office.objects.get(id=int(self.data['office_id']))
        return Exam.objects.create(
            office=office,
            time=self.data['time'],
            desc=self.data['desc'],
            total=self.data['total']
        )



    # PUT /pk/
    def update(self, pk):
        try:
            exam = Exam.objects.get(id=pk)
        except Teacher.DoesNotExist:
            exam = Exam()

        print('hello exam',self.data,exam)
        exam.time = self.data['time']
        exam.desc = self.data['desc']
        exam.total = self.data['total']

        exam.save()
        return exam



    # DELETE /pk/
    def delete(self, pk):
        Exam.objects.get(id=pk).delete()
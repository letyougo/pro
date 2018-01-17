from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from exam.models import Teacher,School,Exam,Office

from exam.api.base import Base 
class ExamResource(Base):
    # Controls what data is included in the serialized output.


    school_preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
    })
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'time':'time',
        'total':'total',
        'desc':'desc',
        'office_name':'office.office_name',
        'office_id':'office.id',
        'status':'status',
        'lock':'lock'
    })

    def is_authenticated(self):

        return True


    # GET /
    def list(self):

        office = Office.objects.get(id=int(self.request.GET['office_id']))
        return Exam.objects.filter(office=office,desc__contains=self.request.GET.get('search',''))

  

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


        exam.time = self.data['time']
        exam.desc = self.data['desc']
        exam.total = self.data['total']
        exam.lock = self.data['lock']
        exam.save()
        return exam



    # DELETE /pk/
    def delete(self, pk):
        Exam.objects.get(id=pk).delete()
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from exam.models import Teacher,School,Exam,Office
from pro.settings import PAGE_SIZE,PAGE_NUM
from django.core.paginator import Paginator

class ExamResource(DjangoResource):
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
        'status':'status'
    })

    def is_authenticated(self):

        return True


    # GET /
    def list(self):

        office = Office.objects.get(id=int(self.request.GET['office_id']))
        return Exam.objects.filter(office=office,desc__contains=self.request.GET.get('search',''))

    def serialize_list(self, data):
        page_size = self.request.GET.get('page_size', PAGE_SIZE)

        paginator = Paginator(data, page_size)  # get value data
        page_num = self.request.GET.get('page_num', PAGE_NUM)

        self.page = paginator.page(page_num)  # This django method takes care of the page number
        list = self.page.object_list
        prepped_data = [self.prepare(item) for item in list]
        final_data = self.wrap_list_response(prepped_data)
        final_data['page'] = dict(
            page_size=int(page_size),
            page_num=int(page_num),
            total=len(data)
        )
        return self.serializer.serialize(final_data)

    def serialize_list(self, data):
        page_size = self.request.GET.get('page_size', PAGE_SIZE)

        paginator = Paginator(data, page_size)  # get value data
        page_num = self.request.GET.get('page_num', PAGE_NUM)

        self.page = paginator.page(page_num)  # This django method takes care of the page number
        list = self.page.object_list
        prepped_data = [self.prepare(item) for item in list]
        final_data = self.wrap_list_response(prepped_data)
        final_data['page'] = dict(
            page_size=int(page_size),
            page_num=int(page_num),
            total=len(data)
        )
        return self.serializer.serialize(final_data)

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

        exam.save()
        return exam



    # DELETE /pk/
    def delete(self, pk):
        Exam.objects.get(id=pk).delete()
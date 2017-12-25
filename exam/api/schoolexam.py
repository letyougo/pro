from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from exam.models import Teacher,School,Schoolexam,Exam
from pro.settings import PAGE_SIZE,PAGE_NUM
from django.core.paginator import Paginator
from django.db.models import Avg,Max,Min,Count
from django.http import JsonResponse

def money(request):
    id = int(request.GET['exam_id'])
    exam = Exam.objects.get(id=id)

    query =Schoolexam.objects.filter(exam=exam)
    num = 0
    for item in query:
        item=item.to_obj()
        num+=int(item['total'])
    return JsonResponse(dict(
        spend=int(num),
        total=int(exam.total),
        exam_id=int(id)
    ))

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

        'total':'total',
        'status':'status'
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
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from django.http import JsonResponse,HttpResponse
from exam.models import Teacher,School
from django.views import View
from pro.settings import PAGE_SIZE,PAGE_NUM
from django.core.paginator import Paginator
import json
import simplejson

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
        list = simplejson.loads(request.body)
        bulk_teacher = [
            Teacher(
                name=item['name'],
                idcard=item['idcard'],
                phone=item['phone'],
                bankcard=item['bankcard'],
                bankinfo=item['bankinfo'],
                school=request.user.school
            )
            for item in list if not Teacher.objects.filter(idcard=item['idcard']).exists()
        ]

        Teacher.objects.bulk_create(bulk_teacher)
        return JsonResponse(dict(error=False,create=len(bulk_teacher)))









def create2(request):
    pass

class TeacherResource(DjangoResource):
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
        'create_time':'create_time'
    })

    def is_authenticated(self):

        return True


    # GET /
    def list(self):
        school = School.objects.get(id=int(self.request.GET['school_id']))

        return Teacher.objects.filter(school=school,name__contains=self.request.GET.get('search',''))

    def serialize_list(self, data):
        page_size = self.request.GET.get('page_size',PAGE_SIZE)

        paginator = Paginator(data, page_size)  # get value data
        page_num = self.request.GET.get('page_num',PAGE_NUM)

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
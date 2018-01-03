from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from exam.models import Teacher,School
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from pro.settings import PAGE_SIZE,PAGE_NUM
from django.core.paginator import Paginator


class SchoolResource(DjangoResource):
    # Controls what data is included in the serialized output.


    school_preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
    })
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name':'name',
        'register_username':'user.username',
        'register_password':'user.password',
        'register_userid':'user.id',
        'admin_name': 'admin_name',
        'admin_phone': 'admin_phone'
    })

    def is_authenticated(self):

        return True


    # GET /
    def list(self):

        return School.objects.filter(name__contains=self.request.GET.get('search',''))

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
        return School.objects.get(id=pk)

    # POST /
    def create(self):
        user = User.objects.create(
            username=self.data['register_username'],
            password=make_password(self.data['register_password'])
        )
        return School.objects.create(
            user=user,
            name=self.data['name'],
            admin_name=self.data['admin_name'],
            admin_phone=self.data['admin_phone']
        )
        # return Teacher.objects.create(
        #     name=self.data['name'],
        #     phone=self.data['phone'],
        #     idcard=self.data['idcard'],
        #     bankcard=self.data['bankcard'],
        #     bankinfo=self.data['bankinfo'],
        #     school=self.request.user.school
        # )

    # PUT /pk/
    def update(self, pk):

        user = User.objects.get(id=int(self.data['register_userid']))

        user.username = self.data['register_username']
        if self.data['change_password']:
            user.password = make_password(self.data['register_password'])
        user.save()
        school = School.objects.get(id=pk)
        school.name=self.data['name']
        school.admin_name = self.data['admin_name']
        school.admin_phone = self.data['admin_phone']
        school.save()


        return school



    # DELETE /pk/
    def delete(self, pk):
        print(pk,School.objects.get(id=pk),'---')
        School.objects.get(id=int(pk)).delete()
 
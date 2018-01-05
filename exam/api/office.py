from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from exam.models import Teacher,Office
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

from exam.api.base import Base 
class officeResource(Base):
    # Controls what data is included in the serialized output.


    office_preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
    })
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'office_name':'office_name',
        'exam_name': 'exam_name',
        'register_username':'user.username',
        'register_password':'user.password',
        'register_userid':'user.id',
        'admin_name':'admin_name',
        'admin_phone':'admin_phone'
    })

    def is_authenticated(self):

        return True


    # GET /
    def list(self):
        return Office.objects.filter(office_name__contains=self.request.GET.get('search', ''))

    # GET /pk/
    def detail(self, pk):
        return Office.objects.get(id=pk)

    # POST /
    def create(self):
        user = User.objects.create(
            username=self.data['register_username'],
            password=make_password(self.data['register_password'])
        )
        return Office.objects.create(
            user=user,
            office_name=self.data['office_name'],
            exam_name=self.data['exam_name'],
            admin_name=self.data['admin_name'],
            admin_phone=self.data['admin_phone']
        )
        # return Teacher.objects.create(
        #     name=self.data['name'],
        #     phone=self.data['phone'],
        #     idcard=self.data['idcard'],
        #     bankcard=self.data['bankcard'],
        #     bankinfo=self.data['bankinfo'],
        #     office=self.request.user.office
        # )

    # PUT /pk/
    def update(self, pk):

        user = User.objects.get(id=int(self.data['register_userid']))

        user.username = self.data['register_username']
        if self.data['change_password']:
            user.password = make_password(self.data['register_password'])

        user.save()

        office = Office.objects.get(id=pk)

        office.office_name=self.data['office_name']
        office.exam_name = self.data['exam_name']
        office.admin_name = self.data['admin_name']
        office.admin_phone = self.data['admin_phone']
        office.save()


        return office



    # DELETE /pk/
    def delete(self, pk):
        Office.objects.get(id=pk).delete()
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from exam.models import Teacher,School
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

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
        'register_userid':'user.id'
    })

    def is_authenticated(self):

        return True


    # GET /
    def list(self):

        return School.objects.all()

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
            name=self.data['name']
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

        school.save()


        return school



    # DELETE /pk/
    def delete(self, pk):
        School.objects.get(id=pk).delete()
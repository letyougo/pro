from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from exam.models import Teacher,School


class SchoolResource(DjangoResource):
    # Controls what data is included in the serialized output.


    school_preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
    })
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name':'name'
    })

    def is_authenticated(self):

        return True
        # print(self.request.user.is_authenticated(),'-=----')
        # return self.request.user.is_authenticated()

    # GET /
    def list(self):

        return School.objects.all()

    # GET /pk/
    def detail(self, pk):
        return Teacher.objects.get(id=pk)

    # POST /
    def create(self):
        print(self.request.user.school,'self.request.user.school')
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
        print(self.data)
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
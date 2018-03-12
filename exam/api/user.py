from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from exam.models import User

from django.contrib.auth.hashers import make_password, check_password

from exam.api.base import Base

class User2(User):
    role = 1

User = User2


class UserResource(Base):
    # Controls what data is included in the serialized output.


    preparer = FieldsPreparer(fields={
        'id': 'id',
        'role':'role',


    })

    def is_authenticated(self):

        return True


    # GET /
    def list(self):
        return User.objects.all()

    # GET /pk/
    def detail(self, pk):
        return User.objects.get(id=pk)

    # POST /
    def create(self):
        pass

    # PUT /pk/
    def update(self, pk):
        pass



    # DELETE /pk/
    def delete(self, pk):
        pass
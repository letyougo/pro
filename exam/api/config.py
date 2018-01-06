from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from exam.models import Config

import simplejson
from exam.api.base import Base 
class ConfigResource(Base):
    # Controls what data is included in the serialized output.


    office_preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
    })
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'key':'key',
        'value': 'value',
        'desc':'desc',
    
    })

    def is_authenticated(self):

        return True


    # GET /
    def list(self):
   
        if 'rate' in self.request.GET:
       
            query = self.request.GET
            base1 = query['base']
            rate1 = query['rate']
  
            base = Config.objects.get(key='base')
            base.value =base1

            rate = Config.objects.get(key="rate")
            rate.value = rate1

            base.save()
            rate.save()
        return Config.objects.all()

    # GET /pk/
    def detail(self, pk):
        pass 

    # POST /
    def create(self):
       pass
       
         

    # PUT /pk/
    def update(self, pk):
       
        pass 



    # DELETE /pk/
    def delete(self, pk):
        Config.objects.get(id=pk).delete()
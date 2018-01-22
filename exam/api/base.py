from restless.dj import DjangoResource
from pro.settings import PAGE_SIZE,PAGE_NUM
from django.core.paginator import Paginator

class Base(DjangoResource):
     

      def serialize_list(self, data):
        if self.request.GET.get('no_page',False):
            prepped_data = [self.prepare(item) for item in data]
            final_data = self.wrap_list_response(prepped_data)
            return self.serializer.serialize(final_data)
        else:

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

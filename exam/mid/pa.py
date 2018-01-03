from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from django.http import JsonResponse
import json


class Row1(MiddlewareMixin):
    def process_request(self,request):
        pass
    def process_response(self,request,response):
        pass
        if 'page_size' in request.GET:
            result = json.loads(response.content.decode('utf-8'))
            pass
            result['page']=dict(
                page_size=request.GET['page_size'],
                page_num=request.GET['page_num'],

            )
            response=JsonResponse(result)
        return response

class Row2(MiddlewareMixin):
    def process_request(self,request):
        pass
        # return HttpResponse("走")
    def process_response(self,request,response):
        pass
        return response

class Row3(MiddlewareMixin):
    def process_request(self,request):
        pass
    def process_response(self,request,response):
        pass
        return response
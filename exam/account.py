from django.shortcuts import render

# Create your views here.

from django.contrib import auth


from django import forms

from django.http.response import HttpResponseRedirect



def login(request):

    if request.method == 'GET':
        return render(request, 'account/login.html')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    # print(user,user.is_active)
    if user and user.is_active:
        u = auth.login(request, user)
        return HttpResponseRedirect(('/'))

        # if user.school:
        #     return HttpResponseRedirect('/school/')
        # elif user.office:
        #     return HttpResponseRedirect('/office/')
        # elif user.center:
        #     return HttpResponseRedirect('/center/')
        #     #

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
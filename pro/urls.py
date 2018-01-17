"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from exam.api.teacher import TeacherResource,teacher2
from exam.api.schoolexam import SchoolExamResource,money
from exam.api.teacherexam import TeacherExamResource,money2
from exam.api.school import SchoolResource
from exam.api.exam import ExamResource
from exam.api.office import officeResource
from exam.api.config import ConfigResource
from exam.account import login,logout
import exam.views as view

import sys
from exam.models import Center,Office,Schoolexam,Teacher,Exam,School,Teacherexam


from django.conf.urls import handler404, handler500




handler404 = 'exam.status.page404'
handler500 = 'exam.status.page500'


# import os
# def back(file):
#     return os.path.dirname(file)

# file = os.path.abspath(__file__)

# file=back(file)
# file=back(file)
# file=back(file)
# sys.path.append(file)

# from django3.contrib import admin as admin2


urlpatterns = [
    path(r'upload/', view.upload),
    path(r'upload2/', view.upload2),
    path('admin/', admin.site.urls),
    path('admin2/', admin.site.urls),
    path('api/teacher/', include(TeacherResource.urls())),
    path('api/schoolexam/', include(SchoolExamResource.urls())),
    path('api/teacherexam/', include(TeacherExamResource.urls())),
    path('api/exam/', include(ExamResource.urls())),
    path('api/school/', include(SchoolResource.urls())),
    path('api/office/', include(officeResource.urls())),
    path('api/config/', include(ConfigResource.urls())),
    path('api/excel/', view.excel),
    path(r'login/', login),

    path(r'logout/', logout),
    path(r'school/', view.school),
    path(r'office/', view.office),
    path(r'center/', view.center),
    path(r'', view.index),

    path('api2/teacher/',teacher2.as_view()),

    path('api2/schoolexam/money/', money),
    path('api2/teacherexam/money/', money2),

    path('api2/excel2/', view.export_users_csv),
    path('api2/export/', view.data_export),
    path('teacherexport', view.teacherexport)
]



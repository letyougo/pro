from django.contrib import admin

# Register your models here.
from .models import School,Center,Office,Teacher,Exam,Schoolexam,Teacherexam
admin.site.register(School)
admin.site.register(Office)
admin.site.register(Center)
admin.site.register(Teacher)
admin.site.register(Exam)
admin.site.register(Schoolexam)
admin.site.register(Teacherexam)
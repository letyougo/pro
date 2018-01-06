from django.contrib import admin

# Register your models here.
from .models import School,Center,Office,Teacher,Exam,Schoolexam,Teacherexam,Config

class school_admin(admin.ModelAdmin):
    list_display = ('user','name','create_time','update_time')

class office_admin(admin.ModelAdmin):
    list_display = ('user','office_name','exam_name','create_time','update_time')

class center_admin(admin.ModelAdmin):
    list_display = ('user','center_name','create_time','update_time')

class teacher_admin(admin.ModelAdmin):
    list_display = ('name','phone','idcard','bankcard','bankinfo','school','create_time','update_time')
    list_filter = ('school',)
    search_fields = ('idcard','name',)

class exam_admin(admin.ModelAdmin):
    list_display = ('office','time','total','desc','status','create_time','update_time')

class school_exam_admin(admin.ModelAdmin):
    list_display = ('exam','school','total','status','create_time','update_time')

class teacher_exam_admin(admin.ModelAdmin):
    list_display = ('teacher','schoolexam','total','create_time','update_time')
    list_filter = ('schoolexam',)

class config_admin(admin.ModelAdmin):
    list_display = ('id','key','value','desc')
admin.site.register(School,school_admin)
admin.site.register(Office,office_admin)
admin.site.register(Center,center_admin)
admin.site.register(Teacher,teacher_admin)
admin.site.register(Exam,exam_admin)
admin.site.register(Schoolexam,school_exam_admin)
admin.site.register(Teacherexam,teacher_exam_admin)
admin.site.register(Config,config_admin)
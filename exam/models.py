# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# import datetime
# import pendulum
# from django.db.models import Sum
# Create your models here.


class School(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,verbose_name=u'注册用户')
    name = models.CharField(max_length=128,null=True,blank=True,verbose_name=u'学校名字')
    admin_name = models.CharField(max_length=128, null=True, blank=True, verbose_name=u'学校管理员')
    admin_phone = models.CharField(max_length=128, null=True, blank=True, verbose_name=u'学校联系电话')
    create_time = models.DateTimeField(auto_now_add=True,null=True,blank=True,verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True,null=True,blank=True,verbose_name=u'更新时间')
    class Meta:
        verbose_name = '学校'
        verbose_name_plural = verbose_name



    def __str__(self):
        return self.name


class Office(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,verbose_name='注册用户')
    office_name = models.CharField(max_length=128,null=True,blank=True,verbose_name='考试办名字')
    exam_name = models.CharField(max_length=128,null=True,blank=True,verbose_name='考试名字')
    admin_name = models.CharField(max_length=128,null=True,blank=True,verbose_name=u'考办管理员')
    admin_phone = models.CharField(max_length=128,null=True,blank=True,verbose_name=u'考办联系电话')
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True,verbose_name='更新时间')
    class Meta:
        verbose_name = '考办'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.office_name


class Center(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,verbose_name='注册用户')
    center_name = models.CharField(max_length=128,null=True,blank=True,verbose_name='中心名字')
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True,verbose_name='更新时间')
    class Meta:
        verbose_name = '中心'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.center_name


class TeacherManager(models.Manager):
    def exist_exam(self,time):
        return self.filter()

class Teacher(models.Model):
    name = models.CharField(max_length=128,null=True,blank=True,verbose_name='老师名字')
    phone = models.CharField(max_length=128,null=True,blank=True,verbose_name='手机号码')
    idcard = models.CharField(max_length=128,null=True,blank=True,verbose_name='身份证',unique=True)
    bankcard = models.CharField(max_length=256,null=True,blank=True,verbose_name='银行卡')
    bankinfo = models.TextField(verbose_name='银行信息')
    school = models.ForeignKey(School,null=True,blank=True,on_delete=models.CASCADE,verbose_name='所在学校')
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True,verbose_name='更新时间')

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name
        ordering = ['-create_time','-update_time']


    def to_obj(self):
        return dict(
            id=self.id,
            name=self.name,
            phone=self.phone,
            idcard=self.idcard,
            bankcard=self.bankcard,
            bankinfo=self.bankinfo,
            school_name=self.school.name,
            school_id=self.school.id,
            create_time=self.create_time,
            update_time=self.update_time
        )

    def __str__(self):
        return self.school.name + '('+ self.name+')'

    def to_excel(self):
        return {
            "姓名":self.name,
            "电话":self.phone,
            '身份证号':self.idcard,
            '银行卡号':self.bankcard,
            '银行信息':self.bankinfo
        }

    @property
    def exam_exist_name(self):
        pass 
    
    def exam_exist_id(self):
        pass
    
    

import time

status_list = (
         ('pass', u'通过'),
         ('checking', u'审核中'),
         ('uncheck', u'未审核'),
    )

class Exam(models.Model):
    office = models.ForeignKey(Office,null=True,blank=True,on_delete=models.CASCADE,verbose_name='所属考试办')
    time = models.DateField(null=True,blank=True,verbose_name='考试时间')
    total = models.CharField(max_length=128,null=True,blank=True,verbose_name='总费用')
    desc = models.TextField(verbose_name='考试描述')
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True,verbose_name='更新时间')
    status = models.CharField(max_length=128,verbose_name=u'状态',choices=status_list,null=True,blank=True)
    lock = models.BooleanField(default=False,verbose_name=u'关闭')
    class Meta:
        verbose_name = '考试'
        verbose_name_plural = verbose_name

    def to_obj(self):
        return dict(
            id=self.id,
            time=self.time,
            desc=self.desc,
            total=self.total,
            office_name=self.office.office_name,
            office_id=self.office.id
        )


    def __str__(self):
        return self.desc

class Schoolexam(models.Model):
    exam = models.ForeignKey(Exam,null=True,blank=True,on_delete=models.CASCADE,verbose_name='所属考试')
    school = models.ForeignKey(School,null=True,blank=True,on_delete=models.CASCADE,verbose_name='监考学校')
    total = models.IntegerField(max_length=256,null=True,blank=True,verbose_name='学校总监考费')
    status = models.CharField(max_length=128, verbose_name=u'状态', choices=status_list, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True,verbose_name='更新时间')

    class Meta:
        verbose_name = '考点考试'
        verbose_name_plural = verbose_name

    def get_name(self):
        return self.exam.desc + ':考点-' + self.school.name

    def __str__(self):
        return self.get_name()

    def to_obj(self):
        return dict(
            id=self.id,
            total=self.total
        )

class Teacherexam(models.Model):
    teacher = models.ForeignKey(Teacher,null=True,blank=True,on_delete=models.CASCADE,verbose_name='监考老师')
    schoolexam = models.ForeignKey(Schoolexam,null=True,blank=True,on_delete=models.CASCADE,verbose_name='在某学校的考试')
    total = models.IntegerField(null=True,blank=True,max_length=256,verbose_name='老师应得监考费')
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True,verbose_name='更新时间')


    # @property
    # def month_total(self):
    #     date_time=self.schoolexam.exam.time
    #     date_time = datetime.datetime.strptime(str(date_time), '%Y-%m-%d')
    #     year = date_time.year
    #     month = date_time.month
    #     start = pendulum.create(year,month,1)
    #     end = start.add(months=1)
    #
    #     start = start.strftime('%Y-%m-%d')
    #     end = end.strftime('%Y-%m-%d')
    #
    #     base = Config.objects.get(key="base")
    #     rate = Config.objects.get(key="rate")
    #
    #
    #     num = self.teacher.teacherexam_set.filter(schoolexam__exam__time__range=[start,end]).aggregate(Sum('total'))['total__sum']
    #
    #     return (float(num)-float(base.value))*float(rate.value)

    class Meta:
        verbose_name = '监考考试'
        verbose_name_plural = verbose_name


    def to_obj(self):


        return dict(
            teacher=self.teacher.to_obj(),
            teacher_id=self.teacher.id,
            exam_id=self.schoolexam.exam.id,
            school_exam_id=self.schoolexam.id,
            total = self.total,
            school_total=self.schoolexam.total,
            update_time = self.update_time,
            create_time = self.create_time,
            desc=self.schoolexam.exam.desc
        )

class Config(models.Model):
    key = models.CharField(max_length=128,unique=True,verbose_name='键')
    value = models.TextField(verbose_name='值')
    desc = models.TextField(null=True,blank=True,verbose_name='描述')


    class Meta:
        verbose_name = '系统配置'
        verbose_name_plural = verbose_name

    def to_obj(self):
        return dict(
            key=self.key,
            value=self.value,
            desc=self.desc
        )
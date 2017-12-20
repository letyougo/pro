# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class School(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,verbose_name=u'注册用户')
    name = models.CharField(max_length=128,null=True,blank=True,verbose_name=u'学校名字')
    create_time = models.DateTimeField(auto_now_add=True,null=True,blank=True,verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True,null=True,blank=True,verbose_name=u'更新时间')
    class Meta:
        verbose_name = '学校端'
        verbose_name_plural = verbose_name



    def __str__(self):
        return self.name


class Office(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,verbose_name='注册用户')
    office_name = models.CharField(max_length=128,null=True,blank=True,verbose_name='考试办名字')
    exam_name = models.CharField(max_length=128,null=True,blank=True,verbose_name='考试名字')
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True,verbose_name='更新时间')
    class Meta:
        verbose_name = '考试办'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.office_name


class Center(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,verbose_name='注册用户')
    center_name = models.CharField(max_length=128,null=True,blank=True,verbose_name='中心名字')
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True,verbose_name='更新时间')
    class Meta:
        verbose_name = '考试中心'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.center_name


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
        verbose_name = '教师列表'
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

import time

class Exam(models.Model):
    office = models.ForeignKey(Office,null=True,blank=True,on_delete=models.CASCADE,verbose_name='所属考试办')
    time = models.DateField(null=True,blank=True,verbose_name='考试时间')
    total = models.CharField(max_length=128,null=True,blank=True,verbose_name='总费用')
    desc = models.TextField(verbose_name='考试描述')
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True,verbose_name='更新时间')


    class Meta:
        verbose_name = '考试信息'
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
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True,verbose_name='更新时间')

    class Meta:
        verbose_name = '考试办分配给学校的考试'
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

    class Meta:
        verbose_name = '学校分配给老师的考试'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.schoolexam.get_name()+'----'+ '监考老师:'+ self.teacher.name+ '-所属学校:' + self.teacher.school.name + ''


    def to_obj(self):


        return dict(
            teacher=self.teacher.to_obj(),
            teacher_id=self.teacher.id,
            exam_id=self.schoolexam.exam.id,

            total = self.total,
            school_total=self.schoolexam.total,
            update_time = self.update_time,
            create_time = self.create_time,
            desc=self.schoolexam.exam.desc
        )







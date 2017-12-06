# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class School(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,)
    name = models.CharField(max_length=128,null=True,blank=True)

    class Meta:
        verbose_name = '学校端'
        verbose_name_plural = verbose_name



    def __str__(self):
        return self.name


class Office(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,)
    office_name = models.CharField(max_length=128,null=True,blank=True)
    exam_name = models.CharField(max_length=128,null=True,blank=True)

    class Meta:
        verbose_name = '考试办'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.office_name


class Center(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,)

    class Meta:
        verbose_name = '考试中心'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    name = models.CharField(max_length=128,null=True,blank=True)
    phone = models.CharField(max_length=128,null=True,blank=True)
    idcard = models.CharField(max_length=256,null=True,blank=True)
    bankcard = models.CharField(max_length=256,null=True,blank=True)
    bankinfo = models.TextField()
    school = models.ForeignKey(School,null=True,blank=True,on_delete=models.CASCADE,)


    class Meta:
        verbose_name = '教师列表'
        verbose_name_plural = verbose_name




    def __str__(self):
        return self.school.name + '('+ self.name+')'

import time

class Exam(models.Model):
    office = models.ForeignKey(Office,null=True,blank=True,on_delete=models.CASCADE,)
    time = models.DateField(null=True,blank=True)
    total = models.CharField(max_length=128,null=True,blank=True)
    desc = models.TextField()



    class Meta:
        verbose_name = '考试信息'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.desc

class Schoolexam(models.Model):
    exam = models.ForeignKey(Exam,null=True,blank=True,on_delete=models.CASCADE)
    school = models.ForeignKey(School,null=True,blank=True,on_delete=models.CASCADE)
    total = models.IntegerField(max_length=256,null=True,blank=True)

    class Meta:
        verbose_name = '考试办分配给学校的考试'
        verbose_name_plural = verbose_name

    def get_name(self):
        return self.exam.desc + ':考点-' + self.school.name

    def __str__(self):
        return self.get_name()

class Teacherexam(models.Model):
    teacher = models.ForeignKey(Teacher,null=True,blank=True,on_delete=models.CASCADE)
    schoolexam = models.ForeignKey(Schoolexam,null=True,blank=True,on_delete=models.CASCADE)
    total = models.IntegerField(null=True,blank=True,max_length=256)

    class Meta:
        verbose_name = '学校分配给老师的考试'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.schoolexam.get_name()+'----'+ '监考老师:'+ self.teacher.name+ '-所属学校:' + self.teacher.school.name + ''







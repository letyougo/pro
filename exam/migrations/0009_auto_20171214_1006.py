# Generated by Django 2.0 on 2017-12-14 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0008_auto_20171207_1050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['-create_time', '-update_time'], 'verbose_name': '教师列表', 'verbose_name_plural': '教师列表'},
        ),
        migrations.AlterField(
            model_name='center',
            name='center_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='中心名字'),
        ),
        migrations.AlterField(
            model_name='center',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='center',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='center',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='注册用户'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='desc',
            field=models.TextField(verbose_name='考试描述'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.Office', verbose_name='所属考试办'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='time',
            field=models.DateField(blank=True, null=True, verbose_name='考试时间'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='total',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='总费用'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='office',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='office',
            name='exam_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='考试名字'),
        ),
        migrations.AlterField(
            model_name='office',
            name='office_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='考试办名字'),
        ),
        migrations.AlterField(
            model_name='office',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='office',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='注册用户'),
        ),
        migrations.AlterField(
            model_name='school',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='学校名字'),
        ),
        migrations.AlterField(
            model_name='school',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='school',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='注册用户'),
        ),
        migrations.AlterField(
            model_name='schoolexam',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='schoolexam',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.Exam', verbose_name='所属考试'),
        ),
        migrations.AlterField(
            model_name='schoolexam',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.School', verbose_name='指派学校'),
        ),
        migrations.AlterField(
            model_name='schoolexam',
            name='total',
            field=models.IntegerField(blank=True, max_length=256, null=True, verbose_name='学校总监考费'),
        ),
        migrations.AlterField(
            model_name='schoolexam',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='bankcard',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='银行卡'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='bankinfo',
            field=models.TextField(verbose_name='银行信息'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='idcard',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='身份证'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='老师名字'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='手机号码'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.School', verbose_name='所在学校'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='teacherexam',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='teacherexam',
            name='schoolexam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.Schoolexam', verbose_name='在某学校的考试'),
        ),
        migrations.AlterField(
            model_name='teacherexam',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.Teacher', verbose_name='监考老师'),
        ),
        migrations.AlterField(
            model_name='teacherexam',
            name='total',
            field=models.IntegerField(blank=True, max_length=256, null=True, verbose_name='老师应得监考费'),
        ),
        migrations.AlterField(
            model_name='teacherexam',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
    ]

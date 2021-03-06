# Generated by Django 2.0 on 2017-12-28 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20171228_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=128, unique=True)),
                ('value', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='teacherexam',
            name='schoolexam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.Schoolexam', verbose_name='在某学校的考试'),
        ),
    ]

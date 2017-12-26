from django.dispatch import receiver
from django.core.signals import request_finished
from django.db.models.signals import pre_save,post_save,post_delete
from exam.models import Schoolexam,Teacherexam
from django.db.models import Sum
# @receiver(request_finished, dispatch_uid="request_finished")
# def my_signal_handler(sender, **kwargs):
#     print("Request finished!================================")
#
#
# def my_signal_handler(sender, **kwargs):
#     print("Request finished!================================")

@receiver(post_save, sender=Schoolexam, dispatch_uid="schoolexam_pre_save")
@receiver(post_delete, sender=Schoolexam, dispatch_uid="schoolexam_pre_save")
def schoolexam_handler(sender,**kwargs):

    exam = kwargs['instance'].exam
    total = Schoolexam.objects.filter(exam=exam).aggregate(Sum('total'))

    if int(total['total__sum']) == int(exam.total):
        exam.status = 'pass'

    else:
        exam.status = 'uncheck'

    exam.save()

@receiver(post_save, sender=Teacherexam, dispatch_uid="teacher_pre_save")
@receiver(post_delete, sender=Teacherexam, dispatch_uid="teacher_pre_save")
def teacherexam_handler(sender,**kwargs):
    schoolexam = kwargs['instance'].schoolexam

    total = Teacherexam.objects.filter(schoolexam=schoolexam).aggregate(Sum('total'))

    if int(total['total__sum']) == int(schoolexam.total):
        schoolexam.status = 'pass'

    else:
        schoolexam.status = 'uncheck'

    schoolexam.save()


# request_finished.connect(my_signal_handler)
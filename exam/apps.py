# -*- coding: utf-8 -*-
from django.apps import AppConfig


class ExamConfig(AppConfig):
    name = 'exam'
    def ready(self):
        # signals are imported, so that they are defined and can be used
        import exam.signals.exam

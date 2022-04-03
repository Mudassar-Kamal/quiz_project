from django.contrib import admin
from .models import *
# from import_export.admin import ExportActionMixin


# class QuizAdmin(ExportActionMixin, admin.ModelAdmin):
#     list_display = ('question', 'correct_ans')
#
# admin.site.register(QuizQuestion, QuizAdmin)

admin.site.register(QuizQuestion)

admin.site.register(Choice)

admin.site.register(Student)

admin.site.register(Result)
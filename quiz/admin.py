from django.contrib import admin
from .models import *
# from import_export.admin import ExportActionMixin


# class QuizAdmin(ExportActionMixin, admin.ModelAdmin):
#     list_display = ('question', 'correct_ans')
#
# admin.site.register(QuizQuestion, QuizAdmin)

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Student)
admin.site.register(ScoreCard)
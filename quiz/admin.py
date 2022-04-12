from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin
from import_export import resources

class question_resources(resources.ModelResource):
    class Meta:
        model = AskedQuestion
        fields = ('student__user__username','question__full_question', 'option_txt_1', 'option_txt_2', 'option_txt_3', 'option_txt_4')
        exclude = ('id')
class AskedQuestionAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('student','question', 'option_txt_1', 'option_txt_2', 'option_txt_3', 'option_txt_4')
    resource_class = question_resources
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Student)
admin.site.register(ScoreCard)
admin.site.register(AskedQuestion,AskedQuestionAdmin)
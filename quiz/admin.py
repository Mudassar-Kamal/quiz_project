from django.contrib import admin
from .models import *


admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Student)
admin.site.register(ScoreCard)
admin.site.register(AskedQuestion)
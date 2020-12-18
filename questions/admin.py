from django.contrib import admin

from .models import Question, Reply


admin.site.register(Question)
admin.site.register(Reply)
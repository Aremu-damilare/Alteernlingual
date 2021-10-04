from django.contrib import admin
from .models import Subject, Topic, SubjectSkill, TopicContent
# Register your models here.

admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(SubjectSkill)
admin.site.register(TopicContent)

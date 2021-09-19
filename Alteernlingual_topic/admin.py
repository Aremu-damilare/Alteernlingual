from django.contrib import admin


# Register your models here.
from .models import Language, LanguageFollow, Skill, SkillFollow, Topic, SubTopic, LanguageOfInteraction, LoiFollow, SubTopicDetails

admin.site.register(Language)
admin.site.register(LanguageFollow)
admin.site.register(Skill)
admin.site.register(SkillFollow)
admin.site.register(Topic)
admin.site.register(SubTopic)
admin.site.register(LanguageOfInteraction)
admin.site.register(SubTopicDetails)
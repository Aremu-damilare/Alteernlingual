from django.contrib import admin


# Register your models here.
from .models import Language, LanguageFollow, LanguageLevel, LevelFollow, Topic, LanguageOfInteraction, LoiFollow,  LoiFollow

admin.site.register(Language)
admin.site.register(LanguageFollow)
admin.site.register(LanguageLevel)
admin.site.register(LevelFollow)
admin.site.register(Topic)
admin.site.register(LanguageOfInteraction)
admin.site.register(LoiFollow)
from django.contrib import admin


# Register your models here.
from .models import Category, EnglishTopic, IgboTopic, HausaTopic, YorubaTopic, FrenchTopic, ArabicTopic

admin.site.register(Category)
admin.site.register(EnglishTopic)
admin.site.register(IgboTopic)
admin.site.register(HausaTopic)
admin.site.register(YorubaTopic)
admin.site.register(FrenchTopic)
admin.site.register(ArabicTopic)
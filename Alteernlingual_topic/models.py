from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import  reverse


class Language(models.Model):
    title = models.CharField(_("title"), max_length=150) 
    description = models.TextField(_("description"), max_length=255, blank=True)

    def all_user(self):
        return list(self.language_follow.values_list('user', flat=True))

    def get_absolute_url(self):
        return reverse('lanuage_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class LanguageLevel(models.Model):
    title = models.CharField(max_length=60)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=True)

    def all_user(self):
        return list(self.level_follow.values_list('user', flat=True))

    def __str__(self):
        return self.title

# class Topic(models.Model):
#     title = models.CharField(max_length=60)
#     level = models.ForeignKey(LanguageLevel, on_delete=models.CASCADE, default=True)

#     def __str__(self):
#         return self.title

class Topic(models.Model):
    title = models.CharField(_("title"), max_length=150)
    main_title =  RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    main_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    language = models.ForeignKey(Language, verbose_name="topic_language", on_delete=models.CASCADE, related_name='follow_language', default=None)
    level = models.ForeignKey(LanguageLevel, verbose_name=("level"), on_delete=models.CASCADE, default=None)

    AR_title = models.TextField(max_length=50000, null=True, blank=True, default=None)
    AR_explanations = models.TextField(null=True, blank=True, default=None)

    EN_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None,)
    EN_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    FR_title = models.TextField(max_length=50000, null=True, blank=True, default=None)
    FR_explanations = models.TextField(null=True, blank=True, default=None)

    HA_title = models.TextField(max_length=50000, null=True, blank=True, default=None)
    HA_explanations = models.TextField(null=True, blank=True, default=None)

    IG_title = models.TextField(max_length=50000, null=True, blank=True, default=None)
    IG_explanations = models.TextField(null=True, blank=True, default=None)

    YO_title = models.TextField(max_length=50000, null=True, blank=True, default=None)
    YO_explanations = RichTextUploadingField(null=True, blank=True, default=None)
    
    published = models.DateField(auto_now_add=True, blank=True, null=True)
    
    slug = models.SlugField(unique=True, max_length=50000, blank=True, null=True)
    read = models.ManyToManyField(User, related_name='read', blank=True)
   
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.main_title)
        return super(Topic, self).save(*args, **kwargs)

    def get_url(self):
       return reverse('detail', args=[self.id])


class readCount(models.Model):
    read = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='read_topics', blank=True, null=True)
    language = models.ForeignKey(Language, verbose_name=("language"), on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    subtopic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)


class LanguageOfInteraction(models.Model):
    loi = models.CharField(max_length=60, default=False, null=True)
    num = models.IntegerField(default=False, null=True)

    def all_user(self):
        return list(self.loi_follow.values_list('user', flat=True))

    def __str__(self):
        return self.loi

    

class LoiFollow(models.Model):
    loi = models.ForeignKey(LanguageOfInteraction, on_delete=models.CASCADE, related_name='loi_follow',
                                 verbose_name='loi', )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class LanguageFollow(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_follow',
                                 verbose_name='language', )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class LevelFollow(models.Model):
    level = models.ForeignKey(LanguageLevel, on_delete=models.CASCADE, related_name='level_follow',
                                 verbose_name='level', )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# class ENReadCount(models.Model):
#     read = models.ForeignKey(EnglishTopic, on_delete=models.CASCADE, related_name='EN_posts')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)



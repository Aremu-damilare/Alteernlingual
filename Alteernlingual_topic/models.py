from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils.text import slugify
from django.contrib.auth.models import User


class Language(models.Model):
    title = models.CharField(_("title"), max_length=150) 
    description = models.TextField(_("description"), max_length=255, blank=True)

    def all_user(self):
        return list(self.language_follow.values_list('user', flat=True))

    def get_absolute_url(self):
        return reverse('lanuage_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=60)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=True)

    def all_user(self):
        return list(self.skill_follow.values_list('user', flat=True))

    def __str__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(max_length=60)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.title


class SubTopic(models.Model):
    title = models.CharField(_("title"), max_length=150)
    main_title =  RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    main_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    language = models.ForeignKey(Language, verbose_name=("language"), on_delete=models.CASCADE, default=None)
    topic = models.ForeignKey(Topic, verbose_name=("topic"), on_delete=models.CASCADE, default=None)

    EN_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None,)
    EN_explanations = RichTextUploadingField(null=True, blank=True, default=None)


    IG_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    IG_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    HA_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    HA_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    YO_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    YO_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    FR_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    FR_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    AR_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    AR_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    published = models.DateField(auto_now_add=True, blank=True, null=True)
    
    slug = models.SlugField(unique=True, max_length=50000, blank=True, null=True)
    read = models.ManyToManyField(User, related_name='EN_posts', blank=True)
   
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.main_title)
        return super(SubTopic, self).save(*args, **kwargs)

class SubTopicDetails(models.Model):
    title = models.CharField(_("title"), max_length=150, blank=True, default=None)
    main_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    language = models.ForeignKey(Language, verbose_name=("language"), on_delete=models.CASCADE, default=None)
    subtopic = models.ForeignKey(SubTopic, verbose_name=("subtopicdetail"), on_delete=models.CASCADE, default=None)

    AR_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    EN_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    FR_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    HA_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    IG_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    YO_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    published = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title



class readCount(models.Model):
    read = models.ForeignKey(SubTopic, on_delete=models.CASCADE, related_name='read_topics', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class LanguageOfInteraction(models.Model):
    loi = models.CharField(max_length=60, default=False, null=True)
    num = models.IntegerField(default=False, null=True)

    def __str__(self):
        return self.loi

    def all_user(self):
        return list(self.loi_follow.values_list('user', flat=True))

class LoiFollow(models.Model):
    loi = models.ForeignKey(LanguageOfInteraction, on_delete=models.CASCADE, related_name='loi_follow',
                                 verbose_name='loi', )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class LanguageFollow(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_follow',
                                 verbose_name='language', )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SkillFollow(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='skill_follow',
                                 verbose_name='skill', )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# class ENReadCount(models.Model):
#     read = models.ForeignKey(EnglishTopic, on_delete=models.CASCADE, related_name='EN_posts')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)



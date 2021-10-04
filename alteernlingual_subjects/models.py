from django.db import models
from django.utils.translation import gettext as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.contrib.auth.models import User
from Alteernlingual_topic.models import Language



class Subject(models.Model):
    title = models.CharField(_("title"), max_length=150) 
    description = models.TextField(_("description"), max_length=255, blank=True)

    def all_user(self):
        return list(self.subject_follow.values_list('user', flat=True))

    def __str__(self):
        return self.title

class SubjectFollow(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_follow',
                                 verbose_name='subject', )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class SubjectSkill(models.Model):
    title = models.CharField(max_length=60)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=True)

    def all_user(self):
        return list(self.subject_skill_follow.values_list('user', flat=True))

    def __str__(self):
        return self.title

class SubjectSkillFollow(models.Model):
    skill = models.ForeignKey(SubjectSkill, on_delete=models.CASCADE, related_name='subject_skill_follow',
                                 verbose_name='subject_skill', )
    user = models.ForeignKey(User, on_delete=models.CASCADE)



from django.urls import  reverse
class Topic(models.Model):
    title = models.CharField(_("title"), max_length=150)
    main_title =  models.TextField(max_length=50000, null=True, blank=True, default=None)
    audio_main_title = models.FileField(upload_to ='audios/', null=True, blank=True, default=None )

    subject = models.ForeignKey(Subject, verbose_name=("subject"), on_delete=models.CASCADE, default=None)
    skill = models.ForeignKey(SubjectSkill, verbose_name=("subject_skill"), on_delete=models.CASCADE, default=None)

    AR_title = models.TextField(max_length=50000, null=True, blank=True, default=None)
    audio_file_ar = models.FileField(upload_to ='audios_en/', null=True, blank=True, default=None)

    EN_title = models.TextField(max_length=50000, null=True, blank=True, default=None,)
    audio_file_en = models.FileField(upload_to ='audios_en/', null=True, blank=True, default=None)

    FR_title = models.TextField(max_length=50000, null=True, blank=True, default=None)
    audio_file_fr = models.FileField(upload_to ='audios_en/', null=True, blank=True, default=None)

    HA_title = models.TextField(max_length=50000, null=True, blank=True, default=None)
    audio_file_ha = models.FileField(upload_to ='audios_en/', null=True, blank=True, default=None)

    IG_title = models.TextField(max_length=50000, null=True, blank=True, default=None)
    audio_file_ig = models.FileField(upload_to ='audios_en/', null=True, blank=True, default=None)

    YO_title = models.TextField(max_length=50000, null=True, blank=True, default=None)
    audio_file_yo = models.FileField(upload_to ='audios_en/', null=True, blank=True, default=None)

    
    
    published = models.DateField(auto_now_add=True, blank=True, null=True)
    
    slug = models.SlugField(unique=True, max_length=50000, blank=True, null=True)
    read = models.ManyToManyField(User, related_name='readsubject', blank=True)
   
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.main_title)
        return super(Topic, self).save(*args, **kwargs)

    # def get_url(self):

    #    return reverse('topic_detail', args=[self.id])

class TopicContent(models.Model):
    title = models.CharField(_("title"), max_length=150, blank=True, default=None)
    main_explanations = models.TextField(null=True, blank=True, default=None)
    audio_main = models.FileField(upload_to ='audios/', null=True, blank=True, default=None )

    subject = models.ForeignKey(Subject, verbose_name=("subject"), on_delete=models.CASCADE, default=None)
    topic = models.ForeignKey(Topic, verbose_name=("subject_topic"), on_delete=models.CASCADE, default=None)

    AR_explanations = models.TextField(null=True, blank=True, default=None)
    audio_file_ar = models.FileField(upload_to ='audios_ar/', null=True, blank=True, default=None)

    EN_explanations = models.TextField(null=True, blank=True, default=None)
    audio_file_en = models.FileField(upload_to ='audios_en/', null=True, blank=True, default=None)

    FR_explanations = models.TextField(null=True, blank=True, default=None)
    audio_file_fr = models.FileField(upload_to ='audios_fr/', null=True, blank=True, default=None)

    HA_explanations = models.TextField(null=True, blank=True, default=None)
    audio_file_ha = models.FileField(upload_to ='audios_ha/', null=True, blank=True, default=None)

    IG_explanations = models.TextField(null=True, blank=True, default=None)
    audio_file_ig = models.FileField(upload_to ='audios_ig/', null=True, blank=True, default=None)

    YO_explanations = models.TextField(null=True, blank=True, default=None)
    audio_file_yo = models.FileField(upload_to ='audios_yo/', null=True, blank=True, default=None)

    published = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title
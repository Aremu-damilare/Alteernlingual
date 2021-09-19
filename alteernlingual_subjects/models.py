from django.db import models
from django.utils.translation import gettext as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.contrib.auth.models import User
from Alteernlingual_topic.models import Language



class Subject(models.Model):
    title = models.CharField(_("title"), max_length=150) 
    description = models.TextField(_("description"), max_length=255, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.title



class Topic(models.Model):
	title = models.CharField(_("title"), max_length=150)
	main_title =  RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
	main_explanations = RichTextUploadingField(null=True, blank=True, default=None)

	language = models.ForeignKey(Language, verbose_name=("language"), on_delete=models.CASCADE, default=None)
	subject = models.ForeignKey(Subject, verbose_name=("subject"), on_delete=models.CASCADE, default=None)

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
	

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
   		if not self.slug:
   			self.slug = slugify(self.title)
   		return super(Topic, self).save(*args, **kwargs)
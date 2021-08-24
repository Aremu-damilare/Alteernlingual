from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils.text import slugify
from django.contrib.auth.models import User



class Category(models.Model):
    title = models.CharField(_("title"), max_length=150)
    description = models.TextField(_("description"), max_length=255, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})


class EnglishTopic(models.Model):
    title = models.CharField(_("title"), max_length=150)
    English_title =  RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    English_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    EN_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None,)
    EN_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    category = models.ForeignKey(Category, verbose_name=("category"), on_delete=models.CASCADE, default=None)

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
            self.slug = slugify(self.English_title)
        return super(EnglishTopic, self).save(*args, **kwargs)

class ENReadCount(models.Model):
    read = models.ForeignKey(EnglishTopic, on_delete=models.CASCADE, related_name='EN_posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class IgboTopic(models.Model):
    title = models.CharField(_("title"), max_length=150)
    Igbo_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    Igbo_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    EN_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    EN_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    category = models.ForeignKey(Category, verbose_name=("category"), on_delete=models.CASCADE, default=None)

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
    read = models.ManyToManyField(User, related_name='IG_posts', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Igbo_title)
        return super(IgboTopic, self).save(*args, **kwargs)

class IGReadCount(models.Model):
    read = models.ForeignKey(IgboTopic, on_delete=models.CASCADE, related_name='IG_posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class HausaTopic(models.Model):
    title = models.CharField(_("title"), max_length=150)
    Hausa_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    Hausa_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    EN_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    EN_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    category = models.ForeignKey(Category, verbose_name=("category"), on_delete=models.CASCADE, default=None)

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

    published = models.DateField(auto_now_add=True,blank=True, null=True)

    slug = models.SlugField(unique=True, max_length=50000, blank=True, null=True)
    read = models.ManyToManyField(User, related_name='HA_posts', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Hausa_title)
        return super(HausaTopic, self).save(*args, **kwargs)

class HAReadCount(models.Model):
    read = models.ForeignKey(HausaTopic, on_delete=models.CASCADE, related_name='HA_posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class YorubaTopic(models.Model):
    title = models.CharField(_("title"), max_length=150)
    Yoruba_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    Yoruba_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    EN_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    EN_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    category = models.ForeignKey(Category, verbose_name=("category"), on_delete=models.CASCADE, default=None)

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

    published = models.DateField(auto_now_add=True,blank=True, null=True)

    slug = models.SlugField(unique=True, max_length=50000, blank=True, null=True)
    read = models.ManyToManyField(User, related_name='YO_posts', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Yoruba_title)
        return super(YorubaTopic, self).save(*args, **kwargs)

class YOReadCount(models.Model):
    read = models.ForeignKey(YorubaTopic, on_delete=models.CASCADE, related_name='YO_posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)




class FrenchTopic(models.Model):
    title = models.CharField(_("title"), max_length=150)
    French_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    French_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    EN_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    EN_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    category = models.ForeignKey(Category, verbose_name=("category"), on_delete=models.CASCADE, default=None)

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
    read = models.ManyToManyField(User, related_name='FR_posts', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.French_title)
        return super(FrenchTopic, self).save(*args, **kwargs)

class FRReadCount(models.Model):
    read = models.ForeignKey(FrenchTopic, on_delete=models.CASCADE, related_name='FR_posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)




class ArabicTopic(models.Model):
    title = models.CharField(_("title"), max_length=150)
    Arabic_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    Arabic_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    EN_title = RichTextUploadingField(max_length=50000, null=True, blank=True, default=None)
    EN_explanations = RichTextUploadingField(null=True, blank=True, default=None)

    category = models.ForeignKey(Category, verbose_name=("category"), on_delete=models.CASCADE, default=None)

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
    read = models.ManyToManyField(User, related_name='AR_posts', blank=True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Arabic_title)
        return super(ArabicTopic, self).save(*args, **kwargs)


class ARReadCount(models.Model):
    read = models.ForeignKey(ArabicTopic, on_delete=models.CASCADE, related_name='AR_posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

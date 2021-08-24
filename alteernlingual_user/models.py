from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.templatetags.static import static
# Create your models here.

class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
    ]

    EN = 1
    IG = 2
    HA = 3
    YO = 4
    FR = 5
    AR = 6
    LTL_CHOICES = [
        (EN, _("English")),
        (IG, _("Igbo")),
        (HA, _("Hausa")),
        (YO, _("Yoruba")),
        (FR, _("French")),
        (AR, _("Arabic")),
    ]
    LOI_CHOICES = [
        (EN, _("English")),
        (IG, _("Igbo")),
        (HA, _("Hausa")),
        (YO, _("Yoruba")),
        (FR, _("French")),
        (AR, _("Arabic")),
    ]

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="profiles/avatars/", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ltl = models.PositiveSmallIntegerField(choices=LTL_CHOICES, null=True, blank=True, default=EN)
    loi = models.PositiveSmallIntegerField(choices=LOI_CHOICES, null=True, blank=True, default=EN)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('img/user-thumb-lg.png')



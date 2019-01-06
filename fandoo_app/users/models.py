from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.conf import settings

from django.db import models
from django.utils.encoding import smart_text as smart_unicode
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return '{self.user.username} Profile'


class Notes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=255)
    done = models.BooleanField(_("Done"), default=False)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Note")
        verbose_name_plural = _("Notes")

    def __unicode__(self):
        return smart_unicode(self.name)

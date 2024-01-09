import uuid
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class ChannelUser(models.Model):
    channel = models.ForeignKey("Channel", verbose_name=_("channel"),on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = _("channel user")
        verbose_name_plural = _("channel users")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("channel_user_detail", kwargs={"pk": self.pk})

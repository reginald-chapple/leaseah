import uuid
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Channel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True, editable=False)
    name = models.CharField(_("name"), max_length=255, null=False, blank=True)
    is_active = models.BooleanField(_("active status"), default=False, blank=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_("users"), blank=True, through="ChannelUser", related_name="channels")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("channel")
        verbose_name_plural = _("channels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("channel_detail", kwargs={"pk": self.pk})
    


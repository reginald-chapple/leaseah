import uuid
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class ChannelMessage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True, editable=False)
    channel = models.ForeignKey("Channel", verbose_name=_("channel"), null=True, on_delete=models.SET_NULL, related_name="messages", blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=_("user"), on_delete=models.CASCADE, related_name="channel_messages", null=False, blank=True)
    content = models.TextField(_("content"), null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("channel message")
        verbose_name_plural = _("channel messages")

    def __str__(self):
        return self.usernsne.name

    def get_absolute_url(self):
        return reverse("channel_message_detail", kwargs={"pk": self.pk})

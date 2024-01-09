from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(_("name"), max_length=75, null=False, blank=True)
    parent = models.ForeignKey("self", verbose_name=_("parent"), on_delete=models.CASCADE,related_name="subcategories", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categories:details", kwargs={"pk": self.pk})

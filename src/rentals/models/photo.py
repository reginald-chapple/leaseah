import uuid
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from .product import Product

class Photo(models.Model):
    slug = models.SlugField(verbose_name=_("slug"),unique=True, default=uuid.uuid1, blank=True)
    url = models.ImageField(verbose_name=_("url"), upload_to='products/%Y/%m/%d/', null=True, blank=True)
    is_default = models.BooleanField(_("default status"), default=False, blank=True)
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE, related_name='photos', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("photo")
        verbose_name_plural = _("photos")

    def __str__(self):
        return str(self.url)
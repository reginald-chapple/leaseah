from datetime import datetime
from datetime import timedelta
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .product import Product

class Rental(models.Model):
    rental_date = models.DateField(_("rental date"), auto_now=False, auto_now_add=False, null=False, blank=True)
    return_date = models.DateField(_("return date"), auto_now=False, auto_now_add=False, null=False, blank=True)
    days_rented = models.PositiveIntegerField(_("days rented"), default=1, blank=True)
    total_cost = models.DecimalField(_("total cost"), max_digits=7, decimal_places=2)
    product = models.ForeignKey(Product, 
        verbose_name=_("product"), 
        on_delete=models.CASCADE,
        related_name="rentals",
        null=False,
        blank=True,
    )
    renter = models.ForeignKey(settings.AUTH_USER_MODEL, 
        verbose_name=_("renter"), 
        on_delete=models.CASCADE, 
        related_name="rentals",
        null=False, 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("rental")
        verbose_name_plural = _("rentals")

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
        return reverse("rentals:details", kwargs={"pk": self.pk})

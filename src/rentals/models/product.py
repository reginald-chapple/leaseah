import json
from datetime import datetime
from datetime import timedelta
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .category import Category

class Product(models.Model):
    name = models.CharField(_("name"), max_length=100, null=False, blank=True)
    description = models.TextField(_("description"), null=False, blank=True)
    daily_rate = models.DecimalField(_("daily rate"), max_digits=6, decimal_places=2, null=False, blank=True)
    deposit = models.DecimalField(_("deposit"), max_digits=6, decimal_places=2, default=0, blank=True)
    is_available = models.BooleanField(_("availability status"), default=False, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, 
        verbose_name=_("owner"), 
        on_delete=models.CASCADE, 
        related_name="products",
        null=False, 
        blank=True
    )
    category = models.ForeignKey(Category, 
        verbose_name=_("category"), 
        on_delete=models.CASCADE, 
        related_name="products",
        null=False, 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
        
    def save(self, *args, **kwargs):
        today = datetime.today()
        title_slugified = slugify(self.name)
        self.slug = f'{title_slugified}-{today:%Y%m%d%M%S%f}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:details", kwargs={"pk": self.pk})
    
    def rented_dates(self):
        rented_dates = set()
        rentals = self.rentals.order_by("-created_at")

        for rental in rentals:
            current_date = rental.rental_date
            while current_date <= rental.return_date:
                rented_dates.add(current_date)
                current_date += timedelta(days=1)

        return list(rented_dates)
    
    def calandar_dates(self):
        rented_dates = []
        rentals = self.rentals.all()
        
        for rental in rentals:
            rented_dates.append({ 
                "title": "Reserved", 
                "start":  rental.rental_date,
                "end": rental.return_date
            })
        return rented_dates

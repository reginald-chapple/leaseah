# Generated by Django 4.2.8 on 2024-01-09 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='renter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to=settings.AUTH_USER_MODEL, verbose_name='renter'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='rentals.category', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='photo',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='rentals.product', verbose_name='product'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='rentals.category', verbose_name='parent'),
        ),
    ]

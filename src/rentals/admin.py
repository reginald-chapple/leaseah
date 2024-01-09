from django.contrib import admin

from rentals.models import Category, Photo, Product, Rental

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Rental)
admin.site.register(Product)
from django.urls import path, include

urlpatterns = [
    path('', include('rentals.urls.categories')),
    path('', include('rentals.urls.products')),
]
from django.urls import include, path

from rentals import views

urlpatterns = [
    path('categories/', include(([
        path('<int:pk>/search/', views.search, name='search'),
    ], 'categories'))),
]
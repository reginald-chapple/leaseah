from django.urls import include, path

from rentals import views

urlpatterns = [
    path('products/', include(([
        path('<int:pk>/reserve/', views.reserve, name='reserve'),
    ], 'products'))),
]
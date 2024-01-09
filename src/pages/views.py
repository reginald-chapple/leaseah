from django.shortcuts import render, redirect

from rentals.models import Category

def home(request):
    # if request.user.is_authenticated and request.user.is_member:
    #     return redirect('users:profile', request.user.slug)
    categories = Category.objects.all()
    template_name='pages/home.html'
    return render(request, template_name, { "categories": categories })


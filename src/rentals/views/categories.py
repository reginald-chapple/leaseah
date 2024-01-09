from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.decorators import member_required

from rentals.models import Category, Product

def search(request, pk):
    if pk == None:
        return redirect("not-found")
    
    category = Category.objects.get(pk=pk)
    
    if category == None:
        return redirect("not-found")
    
    context = { "category": category }
    
    return render(request, "categories/search.html", context)



from datetime import datetime
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.decorators import member_required

from rentals.forms import RentalForm
from rentals.models import Category, Product

def reserve(request, pk):
    if pk == None:
        return redirect("not-found")
    
    product = Product.objects.get(pk=pk)
    form = RentalForm(request.POST or None)
    
    if product == None:
        return redirect("not-found")
    
    context = {}
    
    if form.is_valid():
        c = form.save(commit=False)
        days_rented = c.return_date - c.rental_date
        print(days_rented)
        c.days_rented = int(days_rented.days)
        c.total_cost = product.daily_rate * int(days_rented.days)
        c.renter = request.user
        c.product = product
        c.save()
        return redirect("home")
    
    context["product"] =  product
    context["form"] = form
    
    return render(request, "products/reserve.html", context)
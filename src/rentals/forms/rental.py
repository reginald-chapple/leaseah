from django import forms

from rentals.models import Rental

class RentalForm(forms.ModelForm):
    rental_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    return_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    
    class Meta:
        model = Rental
        fields = ("rental_date","return_date",)

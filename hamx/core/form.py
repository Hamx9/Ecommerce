from django import forms
from django_countries.fields import CountryField

class CheckOut(forms.Form):
    street_adress = forms.CharField()
    apartment_adress = forms.CharField(required=False)
    country = CountryField(blank_label='(select country)')
    zip = forms.CharField()
    same_billing_adress= forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.BooleanField(widget=forms.RadioSelect())
    
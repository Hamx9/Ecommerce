from django import forms
from django_countries.fields import CountryField

PAYMENT_CHOICES=(
('S','Stripe'),
('P','Paypal')
)

class CheckOut(forms.Form):
    street_adress = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control'}))
    apartment_adress = forms.CharField(required=False,widget=forms.TextInput(attrs={ 'class':'form-control'}))
    country = CountryField().formfield()
    zip = forms.CharField()
    same_billing_adress= forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(),choices=PAYMENT_CHOICES)
    
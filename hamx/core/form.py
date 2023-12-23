from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES=(
('S','Stripe'),
('P','Paypal')
)

class CheckOut(forms.Form):
    street_adress = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'Address'}))
    apartment_adress = forms.CharField(required=False,widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'Address 2 (optional)'}))
    country = CountryField(blank_label="(select country)").formfield(widget = CountrySelectWidget(attrs={'class':'custom-select d-block w-100'}))
    zip1 = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control'}))
    same_billing_adress= forms.BooleanField(widget=forms.CheckboxInput(),)
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(),choices=PAYMENT_CHOICES)
    def clean(self):
        cleaned_data = super().clean()
        # Custom form-level validation logic here
        return cleaned_data
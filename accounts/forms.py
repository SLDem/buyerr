from django import forms

from .models import User

import datetime


class EditPersonalForm(forms.ModelForm):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'name-input'}))

    now = datetime.datetime.now()
    current_year = now.year + 1
    birthday = forms.DateField(required=False, widget=forms.SelectDateWidget(attrs={'class': 'birthday-input'},
                                                                             years=range(1940, current_year)))
    gender = forms.NullBooleanField(required=False, widget=forms.Select(choices=[
        (True, 'Male'),
        (False, 'Female')
    ], attrs={'class': 'gender-input'}))

    class Meta:
        model = User
        fields = ('name', 'birthday', 'gender', )


class EditContactsForm(forms.ModelForm):
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'email-input'}))
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'phone-input'}),
                            label=('Phone: Format xxx-xxx-xxxx'))

    class Meta:
        model = User
        fields = ('email', 'phone', )


class EditDeliveryForm(forms.ModelForm):
    delivery_address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'delivery-address-input'}))

    class Meta:
        model = User
        fields = ('delivery_address', )

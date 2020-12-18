from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import User


class SignupForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'signup-name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'signup-email'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'signup-password'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'signup-password'}), label='Confirm Password')

    class Meta:
        model = User
        fields = ('name', 'email', )

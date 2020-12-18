from django.shortcuts import redirect
from django.views.generic import FormView

from .forms import SignupForm
from accounts.models import User


class SignupView(FormView):
    form_class = SignupForm
    template_name = 'authentication/signup.html'

    def form_valid(self, form):
        form.save(commit=False)
        raw_password = form.cleaned_data['password1']
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        user = User.objects.create_user(name=name, email=email, password=raw_password)
        user.save()
        return redirect('login')

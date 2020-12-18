from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView, FormView, UpdateView
from django.views import View

from .models import User
from .forms import EditPersonalForm, EditContactsForm, EditDeliveryForm

from ratings.models import Rating


class ProfileView(DetailView):
    template_name = 'accounts/profile.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.kwargs['pk'])
        context['user'] = user
        if user != self.request.user:
            rating = Rating.objects.filter  (user=user, author=self.request.user).first()
            context['your_rating'] = rating
        return context


class EditPersonalView(UpdateView):
    form_class = EditPersonalForm
    model = User
    template_name = 'accounts/edit-personal.html'

    def form_valid(self, form):
        form.save()
        return redirect('profile', pk=self.request.user.pk)


class EditContactsView(UpdateView):
    form_class = EditContactsForm
    model = User
    template_name = 'accounts/edit-contacts.html'

    def form_valid(self, form):
        form.save()
        return redirect('profile', pk=self.request.user.pk)


class EditDeliveryView(UpdateView):
    form_class = EditDeliveryForm
    model = User
    template_name = 'accounts/edit-delivery.html'

    def form_valid(self, form):
        form.save()
        return redirect('profile', pk=self.request.user.pk)

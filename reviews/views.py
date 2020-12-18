from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DeleteView

from .models import Review
from .forms import ReviewForm

from accounts.models import User


class Reviews(ListView, FormView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/reviews.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Reviews, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.kwargs['pk'])
        reviews = Review.objects.filter(user=user)
        context['user'] = user
        context['reviews'] = reviews
        return context

    def form_valid(self, form):
        review = form.save(commit=False)
        review.author = self.request.user
        user = User.objects.get(pk=self.kwargs['pk'])
        review.user = user
        review.save()
        return redirect('reviews', pk=user.pk)


class DeleteReview(DeleteView):
    model = Review

    def get_success_url(self):
        return reverse_lazy('reviews', kwargs={'pk': self.object.user.pk})

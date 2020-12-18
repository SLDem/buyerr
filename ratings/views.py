from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import DetailView
from django.views import View

from .models import Rating
from accounts.models import User


class LeaveRatingView(View):
    def get(self, request, pk, rating):
        author = request.user
        user = User.objects.get(pk=pk)
        rating = rating
        if rating > 5:
            return HttpResponse('You cant do that')
        current_rating = Rating.objects.filter(author=author, user=user)
        current_rating.delete()
        Rating.objects.create(value=rating, author=author, user=user)
        user_rating = 0
        user_ratings = Rating.objects.filter(user=user)
        for rating in user_ratings:
            user_rating += rating.value
        user_rating = user_rating/user_ratings.count()
        user.rating = round(user_rating, 2)
        user.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))

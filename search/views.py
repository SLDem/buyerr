from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView

from products.models import Product
from .forms import SearchForm


def search_results(request):
    products = Product.objects.all()
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            word = form.cleaned_data['query']
            category = form.cleaned_data['category']
            max_price = form.cleaned_data['max_price']
            min_price = form.cleaned_data['min_price']
            is_available = form.cleaned_data['is_available']
            if word == '' or word is None:
                products = Product.objects.none()
            else:
                products = Product.objects.filter(title__contains=word)
            if category:
                products = products.filter(category=category)
            if max_price:
                products = products.filter(price__lte=max_price)
            if min_price:
                products = products.filter(price__gte=min_price)
            if is_available:
                products = products.filter(is_available=True)
            return render(request, 'search/search_results.html', {'products': products, 'form': form})
    else:
        form = SearchForm()
    return render(request, 'search/search_results.html', {'products': products, 'form': form})


from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView
from django.contrib import messages

from .models import WishlistItem

from products.models import Product


class WishlistView(ListView):
    model = WishlistItem
    template_name = 'wishlist/wishlist.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WishlistView, self).get_context_data(**kwargs)
        wishlist_items = WishlistItem.objects.filter(user=self.request.user)
        context['wishlist_items'] = wishlist_items
        return context


def add_to_wishlist(request, pk):
    product = Product.objects.get(pk=pk)
    WishlistItem.objects.create(user=request.user, product=product)
    messages.add_message(request, messages.INFO, 'Item added to wishlist.')
    return redirect(reverse('product', kwargs={'pk': product.pk}))


class WishlistItemDelete(DeleteView):
    model = WishlistItem

    def get_success_url(self):
        return reverse_lazy('wishlist', kwargs={'pk': self.request.user.pk})
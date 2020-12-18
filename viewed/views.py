from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

from .models import ViewedItem


class ViewedItemsView(ListView):
    model = ViewedItem
    template_name = 'viewed/viewed.html'
    context_object_name = 'viewed_items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ViewedItemsView, self).get_context_data(**kwargs)

        viewed_items = ViewedItem.objects.filter(user=self.request.user).exclude(product__user=self.request.user)[:10]
        context['viewed_items'] = viewed_items
        return context


class DeleteViewedItem(DeleteView):
    model = ViewedItem

    def get_success_url(self):
        return reverse_lazy('viewed', kwargs={'pk': self.request.user.pk})

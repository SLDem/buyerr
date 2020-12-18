from django.shortcuts import render
from django.views.generic import DetailView

from .models import BoughtProduct

from accounts.models import User


class BoughtView(DetailView):
    model = User
    template_name = 'bought/bought.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BoughtView, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.kwargs['pk'])
        bought_products = BoughtProduct.objects.filter(user=user)
        context['bought_products'] = bought_products
        return context
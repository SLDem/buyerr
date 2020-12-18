from django.shortcuts import redirect, reverse, HttpResponse
from django.urls import reverse_lazy

from django.views.generic import ListView, DeleteView
from django.views import View

from .models import Order


class UserOrdersView(ListView):
    model = Order
    template_name = 'orders/orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        orders = Order.objects.filter(user=self.request.user)
        return orders


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('orders', kwargs={'pk': self.request.user.pk})


class ConfirmOrderView(View):
    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        product = order.product
        if order.quantity > product.quantity:
            return HttpResponse('Order quantity exceeds product quantity, please pick a lesser amount.')
        product.quantity -= order.quantity
        product.save()
        if product.quantity <= 0:
            product.is_available = False
            product.quantity = 0
            product.save()
        order.delete()
        return redirect(reverse('orders', kwargs={'pk': self.request.user.pk}))

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('orders/<int:pk>', views.UserOrdersView.as_view(), name='orders'),
    path('delete_order/<int:pk>', views.OrderDeleteView.as_view(), name='delete_order'),
    path('confirm_order/<int:pk>', views.ConfirmOrderView.as_view(), name='confirm_order'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('checkout-session/<int:pk>/', views.checkout_session, name='checkout_session'),
    path('stripe-webhook/', views.stripe_webhook, name='stripe_webhook')
]
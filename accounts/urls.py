from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('edit-personal/<int:pk>/', views.EditPersonalView.as_view(), name='edit_personal'),
    path('edit-contacts/<int:pk>/', views.EditContactsView.as_view(), name='edit_contacts'),
    path('edit-delivery-location/<int:pk>/', views.EditDeliveryView.as_view(), name='edit_delivery_location'),
]

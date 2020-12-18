from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('wishlist/<int:pk>/', views.WishlistView.as_view(), name='wishlist'),
    path('add-to-wishlist/<int:pk>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('delete-wishlist-item/<int:pk>/', views.WishlistItemDelete.as_view(), name='delete_wishlist_item'),
]

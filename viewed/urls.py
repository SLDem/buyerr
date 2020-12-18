from django.urls import path

from . import views


urlpatterns = [
    path('viewed/<int:pk>/', views.ViewedItemsView.as_view(), name='viewed'),
    path('delete-viewed/<int:pk>/', views.DeleteViewedItem.as_view(), name='delete_viewed')
]
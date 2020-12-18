from django.urls import path
from . import views

urlpatterns = [
    path('', views.Messages.as_view(), name='messages'),
    path('private-messages/<int:pk>/', views.PrivateMessages.as_view(), name='private_messages'),
    path('delete-message/<int:pk>/', views.DeleteMessage.as_view(), name='delete_message'),
    path('delete-all-messages/<int:pk>/', views.delete_all_messages, name='delete_all_messages'),
]
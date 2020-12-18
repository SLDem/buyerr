from django.urls import path

from . import views

urlpatterns = [
    path('reviews/<int:pk>/', views.Reviews.as_view(), name='reviews'),
    path('delete-review/<int:pk>/', views.DeleteReview.as_view(), name='delete_review')
]

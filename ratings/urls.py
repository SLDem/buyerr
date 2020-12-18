from django.urls import path

from . import views

urlpatterns = [
    path('leave-rating/<int:pk>/<int:rating>/', views.LeaveRatingView.as_view(), name='leave_rating')
]
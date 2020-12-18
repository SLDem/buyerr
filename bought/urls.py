from django.urls import path

from . import views


urlpatterns = [
    path('bought/<int:pk>/', views.BoughtView.as_view(), name='bought')
]